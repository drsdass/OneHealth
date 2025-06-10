
import pandas as pd

def get_admin_entities(username, csv_path='app/static/admin_entity_access.csv'):
    try:
        df = pd.read_csv(csv_path)
        row = df[df['Admin'].str.lower() == username.lower()]
        if row.empty:
            return []

        # Get all columns except 'Admin'
        entities = row.iloc[0].to_dict()
        return [entity for entity, access in entities.items() if entity != 'Admin' and str(access).strip().lower().startswith('yes')]
    except Exception as e:
        print(f"Error loading access data: {e}")
        return []
