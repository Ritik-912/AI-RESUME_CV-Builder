<template>
  <section class="section-form">
    <h2 class="section-title">Awards</h2>

    <div v-if="store.awards && store.awards.length">
      <div
        v-for="(award, index) in store.awards"
        :key="index"
        class="award-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`award-title-${index}`">Award Title</label>
            <input
              :id="`award-title-${index}`"
              v-model="award.title"
              type="text"
              class="form-control"
              placeholder="e.g., Employee of the Year"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`award-org-${index}`">Organization</label>
            <input
              :id="`award-org-${index}`"
              v-model="award.organization"
              type="text"
              class="form-control"
              placeholder="e.g., ABC Corp"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`award-date-${index}`">Date Earned</label>
            <input
              :id="`award-date-${index}`"
              v-model="award.dateEarned"
              type="date"
              class="form-control"
              required
            />
          </div>
        </form>

        <div class="form-actions">
          <button
            type="button"
            class="btn btn-danger"
            @click="removeAward(index)"
            v-if="store.awards.length > 1"
          >
            Remove
          </button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No awards available.</p>
    </div>

    <div class="form-actions">
      <button type="button" class="btn btn-primary w-full mt-4 text-lg" @click="addAward">
        Add Award
      </button>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue';
import { useResume } from '../index.js';
const store = useResume();

function addAward() {
  store.awards.push({
    title: '',
    organization: '',
    dateEarned: ''
  });
}

function removeAward(index) {
  store.awards.splice(index, 1);
}

onMounted(() => {
  if (!store.awards || store.awards.length === 0) {
    store.awards = [
      {
        title: '',
        organization: '',
        dateEarned: ''
      }
    ];
  }
});
</script>

<style scoped>
.award-entry {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border-radius: 6px;
  background: #f9f9f9;
}

@media (max-width: 600px) {
  .form-actions {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>