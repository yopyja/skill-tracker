<template>
  <div class="glob-container">
    <h2 class="glob-header">Knack</h2>
    <div class="glob-body">
      <PartySelect />
      <GuestListForParty />
    </div>
  </div>
</template>

<script>
import PartySelect from "../components/PartySelect.vue";
import GuestListForParty from "../components/GuestListForParty.vue";
export default {
  name: "PlannerPage",
  components: {
    PartySelect,
    GuestListForParty,
  },
};
</script>
