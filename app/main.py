import streamlit as st
import plotly.express as px

from app.utils import load_clean_data

st.set_page_config(page_title="African Climate Trends", layout="wide")
st.title("African Climate Trend Dashboard")

available_countries = ["ethiopia", "kenya", "sudan", "tanzania", "nigeria"]

selected_countries = st.multiselect(
    "Select countries",
    options=available_countries,
    default=["ethiopia", "kenya"],
)

if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()

data = load_clean_data(selected_countries)
if data.empty:
    st.error("No data loaded. Ensure cleaned CSVs are available in data/.")
    st.stop()

year_min = int(data["Year"].min())
year_max = int(data["Year"].max())
selected_range = st.slider("Select year range", min_value=year_min, max_value=year_max, value=(year_min, year_max))

metric_options = ["T2M", "PRECTOTCORR", "RH2M", "WS2M", "QV2M"]
selected_metric = st.selectbox("Select variable", options=metric_options, index=0)

filtered = data[(data["Year"] >= selected_range[0]) & (data["Year"] <= selected_range[1])].copy()

st.subheader(f"{selected_metric} Monthly Trend")
monthly_metric = (
    filtered.groupby(["Country", filtered["DATE"].dt.to_period("M").astype(str)], as_index=False)[selected_metric]
    .mean()
    .rename(columns={selected_metric: "MonthlyAverage"})
)
monthly_metric = monthly_metric.rename(columns={monthly_metric.columns[1]: "YearMonth"})
fig_metric = px.line(monthly_metric, x="YearMonth", y="MonthlyAverage", color="Country")
st.plotly_chart(fig_metric, use_container_width=True)

monthly_temp = (
    filtered.groupby(["Country", filtered["DATE"].dt.to_period("M").astype(str)], as_index=False)["T2M"]
    .mean()
    .rename(columns={"DATE": "YearMonth", "T2M": "MonthlyAvgT2M"})
)
monthly_temp = monthly_temp.rename(columns={monthly_temp.columns[1]: "YearMonth"})

st.subheader("Temperature Trend (Monthly Average T2M)")
fig_temp = px.line(monthly_temp, x="YearMonth", y="MonthlyAvgT2M", color="Country")
st.plotly_chart(fig_temp, use_container_width=True)

st.subheader("Precipitation Distribution (PRECTOTCORR)")
fig_prec = px.box(filtered, x="Country", y="PRECTOTCORR", color="Country", points=False)
st.plotly_chart(fig_prec, use_container_width=True)
