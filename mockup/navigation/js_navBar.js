$(document).on('click','[data-toggle=sidebar-collapse]', function(){
    SidebarCollapse();
});

function loadBodyContent(page){
    $('#contentBody').load(page);
}
function changeBodyContent(_page){
    window.location.replace(_page);
}
$('#body-row .collapse').collapse('hide'); 

// Collapse/Expand icon
$('#collapse-icon').addClass('fa-angle-double-left'); 

// Collapse click


function SidebarCollapse () {
    console.log("got to collapse function");
    $('.menu-collapsed').toggleClass('d-none');
    $('.sidebar-submenu').toggleClass('d-none');
    $('.submenu-icon').toggleClass('d-none');
    $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');
    
    // Treating d-flex/d-none on separators with title
    var SeparatorTitle = $('.sidebar-separator-title');
    if ( SeparatorTitle.hasClass('d-flex') ) {
        SeparatorTitle.removeClass('d-flex');
    } else {
        SeparatorTitle.addClass('d-flex');
    }
    
    // Collapse/Expand icon
    $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
}

$(document).on('click','#sNavCalendar',function(){
    loadBodyContent("view_calendar.php");
});
$(document).on('click','#navDocs',function(){
    loadBodyContent('./documentWriter/view_docWriter.php');
});
$(document).on('click','#sNavTraining',function(){
    loadBodyContent('./training/userTraining/view_userTraining.php');
});
$(document).on('click','#sDocUpload',function(){
    loadBodyContent('./docForms/view_pageWithPdfAndOthers.php');
});