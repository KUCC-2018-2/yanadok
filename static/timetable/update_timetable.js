$(document).ready(() => {
    $('#btn-search').on('click', loadCourses);
    $('#search-result-table').on('click', addCourseToTimetable);
    $('#course-list-table').on('click', deleteCourseFromTimetable);
    loadTimetable();
    loadCourses();
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function loadTimetable() {
    fetch('/timetable')
        .then((res) => {
            if (res.ok) {
                return res.json();
            }
            throw res.json();})
        .then((body) => {renderTimetable(body.data)})
        .catch((e) => {alert(e.data)});
}


function addCourseToTimetable(event) {
    if (!event.target.classList.contains('btn-add')) {
        return;
    }

    fetch('/timetable', {
        method: 'POST',
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            'course_id': parseInt(event.target.closest('tr').getAttribute('data-id'))
        })
    }).then((res) => {
            if (res.ok) {
                return res.json();
            }
            throw res
        })
        .then((body) => {
            renderTimetable(body.data);
        })
      .catch((res) => {
          handleError(res)
      });
    event.stopPropagation();
}

function renderTimetable(courses) {
    let table = $('#course-list-table');
    let courseHtmls = courses.map((course) => templateCourseRow(course, "delete"));
    showCourseTemplatesToTable(table, courseHtmls);
    colorToTimetable(courses);
}

function colorToTimetable(courses) {
    $(`#timetable .cell`).attr('class', 'cell');
    courses.forEach((course) => {
        let colorClass = 'color-' + Math.floor(Math.random() * 8);
        course['course_times'].forEach((time) => {
            let cell = findCellFromTimetable(time);
            cell.removeClass();
            cell.addClass('cell');
            cell.addClass(colorClass);
        });
    });
}


function findCellFromTimetable(time) {
    let course_days = ['MON', 'TUE', 'WED', 'THU', 'FRI'];
    let column = course_days.indexOf(time['course_day']) + 2;
    let row = time['order'] + 1;
    return $(`#timetable tr:nth-child(${row}) td:nth-child(${column})`);
}

function deleteCourseFromTimetable(event) {
    if (!event.target.classList.contains('btn-delete')) {
        return;
    }
    let timetable_id =  parseInt(event.target.closest('tr').getAttribute('data-id'));
    fetch('/timetable/' + timetable_id, {
        method: 'DELETE',
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    }).then((res) => {
            if (res.ok) {
                return loadTimetable();
            }
            throw res
        })
      .catch((res) => {
          handleError(res)
      });

}

function loadCourses() {
    let url = "/course?";
    url += $.param(getSearchCriteria());
    fetch(url)
        .then((res) => {
            if (res.ok) {
                return res.json();
            }
            throw res;
        })
        .then((body) => {
            let table = $('#search-result-table');
            let courseHtmls = body.data.map((course) => templateCourseRow(course));
            showCourseTemplatesToTable(table, courseHtmls);
        })
        .catch((res) =>
            handleError(res)
        );
}

function handleError(res) {
    if (res.json) {
        res.json().then(e => alert(e.data))
    } else {
        alert('에러가 발생했습니다. 잠시 뒤에 다시 시도해주세요.')
    }
}

function getSearchCriteria() {
    let checked = ['#course_no', '#course_name', '#professor']
        .filter(htmlId => $(htmlId).prop('checked'))[0];

    if (checked != null) {
        return { 'criteria': checked.substring(1, checked.length), "search_keyword": $('#search-input').val() };
    }
    return {}
}

function showCourseTemplatesToTable(table, courses) {
    let rows = courses.join('');
    let head = $(table).find('tr.head');
    $(table).find(".course-row").remove();
    $(rows).insertAfter(head);
}

function templateCourseRow(course, btnType="add") {
    let btn = btnType === "add" ?
        `<td><input type="submit" value="선택" class="btn btn-add"></td>`
        : `<td><input type="submit" value="삭제" class="btn btn-delete"></td>`;
    return `<tr class="course-row"  data-id="${course.course_id}">
              <td>${course.course_no}</td>
              <td>${course.classification}</td>
              <td>${course.course_name}</td>
              <td>${course.professor}</td>
              <td>${course.credit}</td>
              <td>${course.date_classroom}</td>
              ${btn}
            </tr>`;
}