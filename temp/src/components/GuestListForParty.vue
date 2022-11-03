<template>
  <div class="glob-panel">
    <div class="glob-panel-header">GUEST LIST FOR Pug Party 2</div>
    <div class="glob-panel-body">
      <v-card dark id="vueCard">
        <v-data-table
          v-model="singleSelect"
          :headers="headers"
          :items="guestList"
          :single-select="singleSelect"
          item-key="name"
          show-select
          id="vueDataTable"
        >
        </v-data-table>
      </v-card>
    </div>
    <div class="glob-panel-footer">
      <v-btn class="panel-btn info-btn" dark> + Add </v-btn>
      <v-btn class="panel-btn error-btn" dark> - Remove</v-btn>
      <v-btn class="panel-btn success-btn" dark> ✓ Update</v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "GuestListForParty",
  data() {
    return {
      singleSelect: true,
      selected: [],
      headers: [
        {
          text: "Name",
          align: "start",
          value: "name",
        },
        {
          text: "Social Num.",
          value: "ssn",
        },
      ],
      guestList: [
        {
          name: "Freddy Dims",
          ssn: "098-92-2134",
        },
        {
          name: "Archie Cowen",
          ssn: "234-65-2345",
        },
        {
          name: "Tandy Brown",
          ssn: "342-75-7351",
        },
      ],
    };
  },
};
</script>
