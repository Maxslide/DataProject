from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
import pandas as pd
import os


def get_player_shots_data(player_full_name):
    pd.set_option("display.max_rows", None)
    nba_players = players.get_players()
    try:
        current_player = [player for player in nba_players
                          if player["full_name"] == player_full_name][0]
    except:
        return "Player not found."
    if not os.path.isdir(str(os.path.dirname(os.path.abspath(__file__))) + "/../data/" + str(current_player["id"]) + "/"):
        try:
            os.makedirs(str(os.path.dirname(os.path.abspath(__file__))) + "/../data/" + str(current_player["id"]) + "/", mode=0o777, exist_ok=True)
        except OSError as error:
            print(error)
        shots = shotchartdetail.ShotChartDetail(team_id=0, player_id=str(current_player["id"]), context_measure_simple='FGA')
        shots_df = shots.get_data_frames()[0]
        shots_df = shots_df.loc[:, ["TEAM_NAME", "PERIOD", "MINUTES_REMAINING", "SECONDS_REMAINING", "ACTION_TYPE", "SHOT_TYPE", "SHOT_DISTANCE", "LOC_X", "LOC_Y", "SHOT_MADE_FLAG", "GAME_DATE", "HTM", "VTM"]]
        shots_angles = []
        for i in range(shots_df.shape[0]):
            shots_angles += [shots_df.at[i, "LOC_Y"] / shots_df.at[i, "LOC_X"]]
        shots_df.insert(5, "SHOT_ANGLE", shots_angles, True)
        shots_df.drop(["LOC_X", "LOC_Y"], axis=1, inplace=True)
        shots_df.to_json(str(os.path.dirname(os.path.abspath(__file__))) + '/../data/' + str(current_player["id"]) + '/shots_data.json', orient='records')
    return "Player found and data added to database."
