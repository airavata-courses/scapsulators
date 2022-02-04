
function dateconv(dvalue) { 
    var year = dvalue.getFullYear();
    var month = dvalue.getMonth();
    if (month < 10) { month = '0' + month; }
    var day = dvalue.getDate();
    if (day < 10) { day = '0' + day; }
    var hours = dvalue.getHours();
    if (hours < 10) { hours = '0' + hours; }
    var mins = dvalue.getMinutes();
    if (mins < 10) { mins = '0' + mins; }
    var secs = dvalue.getSeconds();
    if (secs < 10) { secs = '0' + secs; }
    var date = year + '-' + month + '-' + day + ' ' + hours + ':' + mins + ':' + secs;
    return date;
}

export {dateconv}