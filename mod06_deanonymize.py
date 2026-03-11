import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    merged = anon_df.merge(aux_df, on=["age", "zip3", "gender"], how="inner")
    # Keep only anon_ids that matched exactly one auxiliary record
    match_counts = merged.groupby("anon_id")["name"].count()
    unique_ids = match_counts[match_counts == 1].index
    unique_matches = merged[merged["anon_id"].isin(unique_ids)][["anon_id", "name"]]
    return unique_matches.rename(columns={"name": "matched_name"}).reset_index(drop=True)


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return len(matches_df) / len(anon_df)
