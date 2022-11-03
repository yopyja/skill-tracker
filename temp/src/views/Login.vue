<template>
    <body>
        <div class="login-container">
            <div class="login-panel block">
                <h2 class="login-header titular">
                    WELCOME
                </h2>
                <div class="login-body">

                    <div class="input-container">
                        <input type="email" placeholder="email" class="email text-input">
                        <div class="input-icon envelope-icon-acount">
                            <span class="fontawesome-envelope scnd-font-color" />
                        </div>
                    </div>


                    <div class="input-container">
                        <input type="password" placeholder="password" class="password text-input">
                        <div class="input-icon password-icon">
                            <span class="fontawesome-lock scnd-font-color" />
                        </div>
                    </div>

                </div>
                <div class="login-footer">
                    <a class="sign-in button" href="../">
                        SIGN IN
                    </a>
                </div>
            </div>
        </div>
    </body>
</template>

<script>
    export default {
      name: "LoginPage",
      data() {
        return {};
      },
    };
    </script>