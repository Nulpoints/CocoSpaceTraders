import json
import altair
import streamlit as st
import pandas as pd
import numpy as np
from pantry_wrapper import *
import os
import spacetraders_client
from spacetraders_client import ApiException, NavigateShipRequest
import datetime

st.session_state.username = None
pantry_id = st.secrets["PANTRY_ID"]

pantry = get_contents(pantry_id, 'SpaceTraders')
def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

st.title("Space Traders StreamLit app")


if st.session_state.username:
    username = st.session_state.username

def shipContainer(ship: spacetraders_client.models.ship):
    container = st.container()
    container.write(ship.symbol)
    with container.expander("Nav"):
        st.write(ship.nav)

    return container


with st.sidebar.form(key="my_form"):
    username = st.text_input("Username")
    submit_button = st.form_submit_button(label="Submit")


if submit_button or st.session_state.username:
    st.session_state.username = username

    configuration = spacetraders_client.Configuration(
                access_token=get_contents(pantry_id, 'SpaceTraders')[username]
            )
    with spacetraders_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        agent_api = spacetraders_client.AgentsApi(api_client)
        fleet_api = spacetraders_client.FleetApi(api_client)
        system_api = spacetraders_client.SystemsApi(api_client)

        try:
            # Get Public Agent
            agent_response = agent_api.get_my_agent().data
            fleet_response = fleet_api.get_my_ships().data
            system_response = system_api.get_system_waypoints(system_symbol="X1-BG67").data

            for ship in fleet_response:
                shipContainer(ship=ship)

            data = []
            for waypoint in system_response:
                data.append({'symbol': waypoint.symbol, 'x': waypoint.x, 'y': waypoint.y, "type": waypoint.type})
            system_df = pd.DataFrame(data)
            st.dataframe(system_df)
            event = st.vega_lite_chart(
                system_df,
                {
                    "mark": {"type": "circle"},
                    "encoding": {
                        "x": {"field": "x", "type": "quantitative"},
                        "y": {"field": "y", "type": "quantitative"},
                        "tooltip": [{"field": "symbol", "type": "nominal"},
                                    {"field": "type", "type": "nominal"}]
                    },
                },
            )

        except ApiException as e:
            print("Exception when calling AgentsApi->get_agent: %s\n" % e)
            st.write(json.loads(e.body)['error']['message'])
