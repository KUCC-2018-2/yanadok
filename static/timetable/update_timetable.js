$(document).ready(() => {
    $('#btn-search').on('click', getCourses);
});


function getCourses() {
    let url = "/course?";
    url += $.param(getSearchCriteria());
    fetch(url)
        .then((res) => {
            if (res.ok) {
                return res.json();
            }
            throw '강의 정보 검색에 실패했습니다. 잠시 뒤에 다시 시도해주세요.';
        })
        .then((body) => {
            $(".search-result-row").remove();
            showCourseSearchResult(body.data);
        })
        .catch((e) => alert(e));
}

function getSearchCriteria() {
    let checked = ['#course_no', '#course_name', '#professor']
        .filter(htmlId => $(htmlId).prop('checked'))[0];

    if (checked != null) {
        return { 'criteria': checked.substring(1, checked.length), "search_keyword": $('#search-input').val() };
    }
    return {}
}

function showCourseSearchResult(courses) {
    let rows = courses.map((course) => templateCourseRow(course));
    let head = $('#search-result-table tr.head');
    rows.reverse().forEach((row) => {$(row).insertAfter(head)});
}

function templateCourseRow(course) {
    return `<tr class="search-result-row">
              <td>${course.course_no}</td>
              <td>${course.classification}</td>
              <td>${course.course_name}</td>
              <td>${course.professor}</td>
              <td>${course.credit}</td>
              <td>${course.date_classroom}</td>
              <td><input type="submit" value="삭제" class="delete"></td>
            </tr>`;
}

function updateTimetableRequest() {
    fetch("/test").then((res) => {

    });
}