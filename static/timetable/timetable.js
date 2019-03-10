$(document).ready(() => {
    loadTimetable(renderTimetable);
});

function findCellFromTimetable(time) {
    let course_days = ['MON', 'TUE', 'WED', 'THU', 'FRI'];
    let column = course_days.indexOf(time['course_day']) + 2;
    let row = time['order'] + 1;
    return $(`#timetable tr:nth-child(${row}) td:nth-child(${column})`);
}

function renderTimetable(courses) {
    courses.forEach((course, index) => {
        let colorClass = 'color-' + index;
        course['course_times'].forEach((time) => {
            let cell = findCellFromTimetable(time);
            cell.addClass(colorClass);
            cell.html(`<a href="/board/${course['course_id']}" class="text-white">${course['course_name']}</a>`);
        });
    });
}

function loadTimetable(callback) {
    fetch('/timetable')
        .then((res) => {
            if (res.ok) {
                return res.json();
            }
            throw res.json();})
        .then((body) => {callback(body.data)})
        .catch((e) => {alert(e.data)});
}
