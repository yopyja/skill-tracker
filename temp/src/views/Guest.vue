<template>
  <body>
    <div class="account block">
      <h2 class="titular">Guest Management</h2>
      <div>
        <div class="input-container">
          <input type="text" placeholder="First" class="text text-input" />
          <div class="input" />
        </div>
        <div class="input-container">
          <input type="text" placeholder="Last" class="text text-input" />
          <div class="input" />
        </div>
        <a class="sign-in button" href="#22">Create Guest</a>
      </div>
    </div>
  </body>
</template>

<script>
  export default {
    name: "GuestPage",
    data() {
      return {};
    },
  };
  </script>