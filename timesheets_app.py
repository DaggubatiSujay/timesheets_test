import streamlit as st
import calendar
import datetime

st.set_page_config(page_title="Timesheet Calendar", layout="wide")
st.title("🗓️ Editable Timesheet Calendar")

# Initialize session state for current date view
if "current_year" not in st.session_state:
    st.session_state.current_year = datetime.date.today().year
if "current_month" not in st.session_state:
    st.session_state.current_month = datetime.date.today().month
if "timesheet" not in st.session_state:
    st.session_state.timesheet = {}

# Utility function to format month name
def get_month_year_label(year, month):
    return f"{calendar.month_name[month]} {year}"

# Handle month navigation
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("⬅️", key="prev_month"):
        st.session_state.current_month -= 1
        if st.session_state.current_month == 0:
            st.session_state.current_month = 12
            st.session_state.current_year -= 1
with col3:
    if st.button("➡️", key="next_month"):
        st.session_state.current_month += 1
        if st.session_state.current_month == 13:
            st.session_state.current_month = 1
            st.session_state.current_year += 1
with col2:
    st.markdown(
        f"<h3 style='text-align: center'>{get_month_year_label(st.session_state.current_year, st.session_state.current_month)}</h3>",
        unsafe_allow_html=True,
    )

# Extract current view info
year = st.session_state.current_year
month = st.session_state.current_month
num_days = calendar.monthrange(year, month)[1]
first_weekday = datetime.date(year, month, 1).weekday()  # Monday = 0

# Initialize or update the timesheet structure for the current month
month_key = f"{year}-{month:02d}"
if month_key not in st.session_state.timesheet:
    st.session_state.timesheet[month_key] = {day: 0 for day in range(1, num_days + 1)}

# Calendar headers
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
header_cols = st.columns(7)
for i, day_name in enumerate(days_of_week):
    with header_cols[i]:
        st.markdown(f"**{day_name}**", unsafe_allow_html=True)

# Build the calendar grid
day = 1
while day <= num_days:
    week_cols = st.columns(7)
    for i in range(7):
        if (day == 1 and i < first_weekday) or day > num_days:
            with week_cols[i]:
                st.markdown(" ")
        else:
            with week_cols[i]:
                st.markdown(
                    f"""
                    <div style='border:1px solid #ccc; padding:10px; border-radius:6px; text-align:center'>
                        <strong>{day}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.session_state.timesheet[month_key][day] = st.number_input(
                    label="",
                    min_value=0,
                    max_value=24,
                    value=st.session_state.timesheet[month_key][day],
                    step=1,
                    key=f"{month_key}-day-{day}",
                )
                day += 1

# Optional summary
st.markdown("---")
st.subheader("🧾 Summary of Hours")
st.write(st.session_state.timesheet[month_key])
