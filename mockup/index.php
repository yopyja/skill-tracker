	
<!DOCTYPE html>
<html>
<?php //phpinfo() ?>
 
 //include "data_for_training_tasks.php"; 
 
?>
<script>
    $(document).ready(function(){
        $('#contentBody').load('./docForms/view_pageWithPdfAndOthers.php');  
    });
</script>

    <body id="top">
    <nav class="navbar navbar-expand-md navbar-dark bg-primary">
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNavDropdown">
        <span class="navbar-toggler-icon"></span>
    </button>
    <a class="navbar-brand" href="#">
        <img src="https://v4-alpha.getbootstrap.com/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">
        <span class="menu-collapsed">Brand</span>
    </a>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#top">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Dropdown</a>
                <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Separated link</a></li>
                </ul>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#top">Pricing</a>
            </li>
            <!-- This menu is hidden in bigger devices with d-sm-none. 
        The sidebar isn't proper for smaller screens imo, so this dropdown menu can keep all the useful sidebar itens exclusively for smaller screens  -->
            <li class="nav-item dropdown d-sm-block d-md-none">
                <a class="nav-link dropdown-toggle" href="#" id="smallerscreenmenu" data-toggle="dropdown"> Menu </a>
                <div class="dropdown-menu" aria-labelledby="smallerscreenmenu">
                    <a class="dropdown-item" href="#top">hjsahgjsa</a>
                    <a class="dropdown-item" href="#top">Profile</a>
                    <a class="dropdown-item" href="#top">Tasks</a>
                    <a class="dropdown-item" href="#top">Etc ...</a>
                </div>
            </li><!-- Smaller devices menu END -->
        </ul>
    </div>
</nav>


<!-- START OF SIDE NAV BAR -->

        <div class="row" id="body-row">
            <div id="sidebar-container" class="sidebar-expanded d-none d-md-block">
                <!-- d-* hiddens the Sidebar in smaller devices. Its itens can be kept on the Navbar 'Menu' -->
                <!-- Bootstrap List Group -->
                <ul class="list-group">
                    <!-- Separator with title -->
                    <li class="list-group-item sidebar-separator-title text-muted d-flex align-items-center menu-collapsed">
                        <small>MAIN MENU</small>
                    </li>
                    <!-- /END Separator -->
                    <!-- Menu with submenu -->
                    <a href="#submenu1" data-toggle="collapse" aria-expanded="false" class="bg-dark list-group-item list-group-item-action flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-user fa-fw mr-3"></span>
                            <span class="menu-collapsed">Dashboard</span>
                            <span class="submenu-icon ml-auto"></span>
                        </div>
                    </a>
                    <!-- Submenu content -->
                    <div id='submenu1' class="collapse sidebar-submenu">
                        <a href="#" class="list-group-item list-group-item-action bg-dark text-white" id="navDocs">
                            <span class="menu-collapsed">Documents</span>
                        </a>
                        <a href="#" class="list-group-item list-group-item-action bg-dark text-white">
                            <span class="menu-collapsed">Reports</span>
                        </a>
                        <a href="#" class="list-group-item list-group-item-action bg-dark text-white">
                            <span class="menu-collapsed">Tables</span>
                        </a>
                    </div>
                    <a href="#submenu2" data-toggle="collapse" aria-expanded="false" class="bg-dark list-group-item list-group-item-action flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-user fa-fw mr-3"></span>
                            <span class="menu-collapsed">Profile</span>
                            <span class="submenu-icon ml-auto"></span>
                        </div>
                    </a>
                    <!-- Submenu content -->
                    <div id='submenu2' class="collapse sidebar-submenu">
                        <a href="#" class="list-group-item list-group-item-action bg-dark text-white">
                            <span class="menu-collapsed">Settings</span>
                        </a>
                        <a href="#" id="getTry" isHeader="1" class="list-group-item list-group-item-action bg-dark text-white">
                            <span class="menu-collapsed" >Password</span>
                        </a>
                    </div>
                        <a id="sNavTraining" href="#" class="bg-dark list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-start align-items-center" >
                                <span class="fa fa-tasks fa-fw mr-3"></span>
                                <span class="menu-collapsed">Training</span>
                            </div>
                        </a>
                    <!-- Separator with title -->
                    <li class="list-group-item sidebar-separator-title text-muted d-flex align-items-center menu-collapsed">
                        <small>OPTIONS</small>
                    </li>
                    <!-- /END Separator -->
                    <a  id="sNavCalendar" href="#" class="bg-dark list-group-item list-group-item-action">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-calendar fa-fw mr-3"></span>
                            <span class="menu-collapsed">Calendar</span>
                        </div>
                    </a>
                    <a href="#" class="bg-dark list-group-item list-group-item-action">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-envelope fa-fw mr-3"></span>
                            <span class="menu-collapsed">Messages <span class="badge badge-pill badge-primary ml-2">5</span></span>
                        </div>
                    </a>
                    <a id="sDocUpload" href="#" class="bg-dark list-group-item list-group-item-action">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-envelope fa-fw mr-3"></span>
                            <span class="menu-collapsed">Apply Now!</span>
                        </div>
                    </a>
                    <!-- Separator without title -->
                    <li class="list-group-item sidebar-separator menu-collapsed"></li>
                    <!-- /END Separator -->
                    <a href="#" class="bg-dark list-group-item list-group-item-action">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-question fa-fw mr-3"></span>
                            <span class="menu-collapsed">Help</span>
                        </div>
                    </a>
                    <a  data-toggle="sidebar-collapse" class="bg-dark list-group-item list-group-item-action d-flex align-items-center">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span id="collapse-icon" class="fa fa-angle-double-left mr-3"></span>
                            <span id="collapse-text" class="menu-collapsed">Collapse</span>
                        </div>
                    </a>
                </ul><!-- List Group END-->
            </div>



            <div id="contentBody" class="col-md-10">
            </div>
        </div>
    </body>



    <div class="modal fade" id="editEventModal" tabindex="-1" rold="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Modal Header</h4>
                    <button class="btn close" data-dismiss="modal">&times;</button>  
                </div>
                <div class="modal-body form-group">
                    <input class="form-control" id="modal_titleInput">
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button id="modal_eventSave" type="button" class="btn btn-primary" data-dismiss="modal">Save</button>
                </div>
            </div>
        </div>
    </div>
</html>



