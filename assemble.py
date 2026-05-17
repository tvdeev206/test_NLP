from distance_calc import cal_distance
from findvehicle import get_vehicle
from schema import Coordinates, prompt
import pandas as pd

def find_vehicle(origin: Coordinates, text: prompt):
    df = pd.read_csv("data/rental_recommendations_flat.csv")

    target_ids = get_vehicle(text.prompt)

    matched_df = df[df['vehicle_id'].isin(target_ids)].copy()

    if matched_df.empty:
        return matched_df

    matched_df['distance_km'] = cal_distance(
        origin.lat, origin.lon,
        matched_df['lat'], matched_df['lng']
    )

    final_df = matched_df[matched_df['distance_km'] <= 50].copy()


    final_df = final_df.sort_values(by='distance_km')

    return final_df


