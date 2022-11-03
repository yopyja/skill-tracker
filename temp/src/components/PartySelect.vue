<template>
  <div class="glob-panel">
    <div class="glob-panel-header">PARTY SELECTION</div>
    <div class="glob-panel-body">
      <v-card dark id="vueCard">
        <v-card-title>
          <v-text-field
            class="vue-text-field"
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :items-per-page="3"
          :headers="header"
          :items="partyList"
          :single-select="singleSelect"
          :search="search"
          show-select
          loading
          loading-text="Loading... Please wait"
          id="vueDataTable"
        >
        </v-data-table>
      </v-card>
    </div>
    <div class="glob-panel-footer">
      <div class="text-center">
        <v-btn class="panel-btn info-btn" dark> Load </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PartySelect",
  data() {
    return {
      search: "",
      singleSelect: true,
      selected: [],
      header: [
        {
          text: "Parties",
          align: "start",
          sortable: false,
          value: "partyName",
        },
      ],
      partyList: [
        {
          partyName: "Pug Party 1",
        },
        {
          partyName: "Pug Party 2",
        },
        {
          partyName: "Pug Party 3",
        },
        {
          partyName: "Pug Party 4",
        },
        {
          partyName: "Pug Party 5",
        },
      ],
    };
  },
};
</script>
