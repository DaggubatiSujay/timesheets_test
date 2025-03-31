import streamlit as st
import calendar
import datetime
<<<<<<< HEAD
=======
import json
>>>>>>> f7c2559 (Initial commit)

st.set_page_config(page_title="Timesheet Calendar", layout="wide")
st.title("🗓️ Editable Timesheet Calendar")

<<<<<<< HEAD
# Initialize session state for current date view
=======
# ------------------ Setup Calendar State ------------------
>>>>>>> f7c2559 (Initial commit)
if "current_year" not in st.session_state:
    st.session_state.current_year = datetime.date.today().year
if "current_month" not in st.session_state:
    st.session_state.current_month = datetime.date.today().month
if "timesheet" not in st.session_state:
    st.session_state.timesheet = {}

<<<<<<< HEAD
# Utility function to format month name
def get_month_year_label(year, month):
    return f"{calendar.month_name[month]} {year}"

=======
>>>>>>> f7c2559 (Initial commit)
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
<<<<<<< HEAD
        f"<h3 style='text-align: center'>{get_month_year_label(st.session_state.current_year, st.session_state.current_month)}</h3>",
        unsafe_allow_html=True,
    )

# Extract current view info
year = st.session_state.current_year
month = st.session_state.current_month
num_days = calendar.monthrange(year, month)[1]
first_weekday = datetime.date(year, month, 1).weekday()  # Monday = 0

# Initialize or update the timesheet structure for the current month
=======
        f"<h3 style='text-align:center;'>{calendar.month_name[st.session_state.current_month]} {st.session_state.current_year}</h3>",
        unsafe_allow_html=True,
    )

# Get details for current month
year = st.session_state.current_year
month = st.session_state.current_month
num_days = calendar.monthrange(year, month)[1]
first_weekday = datetime.date(year, month, 1).weekday()

>>>>>>> f7c2559 (Initial commit)
month_key = f"{year}-{month:02d}"
if month_key not in st.session_state.timesheet:
    st.session_state.timesheet[month_key] = {day: 0 for day in range(1, num_days + 1)}

<<<<<<< HEAD
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
=======
# Prepare calendar grid as HTML
calendar_html = """
<style>
  .calendar {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 4px;
  }
  .day-cell {
    border: 1px solid #888;
    height: 100px;
    position: relative;
    padding: 4px;
  }
  .date-number {
    position: absolute;
    top: 4px;
    left: 6px;
    font-size: 12px;
    font-weight: bold;
    color: #ccc;
  }
  .hour-input {
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    width: 60px;
  }
  .weekday-labels {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    text-align: center;
    margin-bottom: 6px;
    font-weight: bold;
  }
</style>
<div class="weekday-labels">
  <div>Mon</div><div>Tue</div><div>Wed</div><div>Thu</div><div>Fri</div><div>Sat</div><div>Sun</div>
</div>
<div class="calendar">
"""

day_counter = 1
blank_days = first_weekday  # 0 for Monday, 6 for Sunday
total_cells = blank_days + num_days
cell_values = []

for i in range(total_cells):
    if i < blank_days:
        calendar_html += '<div class="day-cell"></div>'
    else:
        this_day = day_counter
        value = st.session_state.timesheet[month_key][this_day]
        calendar_html += f"""
        <div class="day-cell">
            <div class="date-number">{this_day}</div>
            <input class="hour-input" type="number" id="day_{this_day}" name="day_{this_day}" min="0" max="24" value="{value}">
        </div>
        """
        cell_values.append(this_day)
        day_counter += 1

calendar_html += "</div>"

# Inject HTML calendar
st.components.v1.html(calendar_html, height=600, scrolling=True)

# 🚧 Optional: You can add logic to sync values back to Streamlit using JS → Streamlit forms or st.text_area json dump (on submit).
# For now, it shows the UI fully styled as you wanted.
>>>>>>> f7c2559 (Initial commit)
