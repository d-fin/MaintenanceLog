window.onload() = function () {
    const element = document.getElementById('upcomingTableBody');
    element.removeChild();
    element.remove();
    /* document.getElementById('behindTableRow').style.visibility = 'visible';
    document.getElementById('upcomingTableRow').style.visibility = 'hidden'; */
};

function onDataSelect2() {
    var tasks = document.getElementById('upcomingDropdown').innerHTML;
    var table = document.getElementById('behindUpcomingTable').removeChild()
    /*  var tasks = document.getElementById('upcomingDropdown').innerHTML;
     console.log(tasks)
     if(tasks == 'Upcoming'){
         document.getElementById('behindTableRow').style.visibility = 'hidden';
         document.getElementById('upcomingTableRow').style.visibility = 'visible';
     } */
};

function onDataSelect() {
    var tasks = document.getElementById('behindDropdown').innerHTML;
    console.log(tasks)
    if (tasks == 'Behind') {
        document.getElementById('behindTableRow').style.visibility = 'visible';
        document.getElementById('upcomingTableRow').style.visibility = 'hidden';
    }
};