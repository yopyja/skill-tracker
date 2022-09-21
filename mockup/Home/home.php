<!DOCTYPE html>
<html>
    <head>
        <link href="https://cdn.datatables.net/1.12.1/css/dataTables.bootstrap5.min.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
        
        <script src="https://code.jquery.com/jquery-3.6.1.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        <script src="https://cdn.datatables.net/1.12.1/js/jquery.dataTables.min.js"></script>
        <script src="https://cdn.datatables.net/1.12.1/js/dataTables.bootstrap5.min.js"></script>
        <script src="./Data"></script>
        <script>
            var result = [];
            for(var i in dataSet){
                result.push([dataSet[i].first_name, dataSet[i].last_name, dataSet[i].email, dataSet[i].skill, dataSet[i].team]);
            }
            $(document).ready(function () {
                $('#example').DataTable({
                    data: result,
                    columns: [
                        { title: 'First Name' },
                        { title: 'Last Name' },
                        { title: 'Email' },
                        { title: 'Team' },
                        { title: 'Skill' },
                    ],
                });
            });
            $(document).on('click', '#mybtn', function(){
                $('#thide-1').toggle();
                $('#thide-2').toggle();
            });
        </script>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg bg-dark navbar-dark mb-5">
            <div class="container-fluid">
              <a class="navbar-brand" href="#">Navbar</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="../mockup/Users/view_users.html">Link</a>
                  </li>
                  <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Dropdown
                    </a>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="#">Action</a></li>
                      <li><a class="dropdown-item" href="#">Another action</a></li>
                      <li><hr class="dropdown-divider"></li>
                      <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link disabled">Disabled</a>
                  </li>
                </ul>
                <form class="d-flex" role="search">
                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
              </div>
            </div>
        </nav>
        <div class="row">
            <div class="col-md-3">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="card-link">Card link</a>
                        <a href="#" class="card-link">Another link</a>
                    </div>
                    <div class="card-footer">
                        <button id="mybtn" class="btn btn-warning">Show/hide</button>
                    </div>
                </div>
            </div>
            <div class="col-md-9">
                <div id="thide-1"> <table id="example" class="display table table-striped table-condensed" width="100%"></table></div>
                <div id="thide-2" style="display:none"> <H1>LUNCH BREAK! Be back in a few</H1></div>
            </div>
        </div>
    </body>
</html>