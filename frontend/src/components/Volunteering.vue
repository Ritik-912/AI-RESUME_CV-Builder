<template>
  <section class="section-form">
    <h2 class="section-title">Volunteering & Leadership</h2>

    <div v-if="store.volunteering && store.volunteering.length">
      <div
        v-for="(position, index) in store.volunteering"
        :key="index"
        class="position-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`organization-${index}`">Organization<span class="required-asterisk">*</span></label>
            <input
              :id="`organization-${index}`"
              v-model.trim="position.organization"
              type="text"
              class="form-control"
              placeholder="Enter organization name"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`role-${index}`">Role/Position<span class="required-asterisk">*</span></label>
            <input
              :id="`role-${index}`"
              v-model.trim="position.role"
              type="text"
              class="form-control"
              placeholder="Enter your role"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`location-${index}`">Location<span class="required-asterisk">*</span></label>
            <input
              :id="`location-${index}`"
              v-model.trim="position.location"
              type="text"
              class="form-control"
              placeholder="Enter location"
              required
            />
          </div>

          <div class="form-group-inline">
            <div class="form-group">
              <label :for="`startDate-${index}`">Start Date<span class="required-asterisk">*</span></label>
              <input
                :id="`startDate-${index}`"
                v-model="position.startDate"
                type="month"
                class="form-control"
                required
              />
            </div>

            <div class="form-group">
              <label :for="`endDate-${index}`">End Date</label>
              <input
                :id="`endDate-${index}`"
                v-model="position.endDate"
                type="month"
                class="form-control"
                required
              />
            </div>
          </div>

          <div class="form-group">
            <label :for="`description-${index}`">Description</label>
            <textarea
            :id="`description-${index}`"
            v-model.trim="position.description"
            class="form-control"
            placeholder="Enter a brief description of your role and responsibilities"
            rows="4"
            ></textarea>
          </div>

          <button
            v-if="store.volunteering.length > 0"
            @click="removePosition(index)"
            type="button"
            class="btn btn-danger w-full mt-2"
          >
            Remove Position
          </button>
        </form>
      </div>
    </div>
    <div v-else class="text-center text-muted">
      <p>No volunteering positions added yet.</p>
    </div>

    <button
      @click="addPosition"
      type="button"
      class="btn btn-primary w-full mt-4 text-lg"
    >
      Add New Volunteering Position
    </button>
  </section>
</template>

<script setup>
import { useResume } from '../index.js';

const store = useResume();

const addPosition = () => {
  store.volunteering.push({
    organization: '',
    role: '',
    location: '',
    startDate: '',
    endDate: '',
    description: ''
  });
};

const removePosition = (index) => {
  if (store.volunteering.length > 0) {
    store.volunteering.splice(index, 1);
  }
};
</script>

<style scoped>
.position-entry {
  margin-bottom: var(--space-lg);
  padding: var(--space-md);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  background-color: var(--color-white);
  box-shadow: var(--shadow-md);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.position-entry:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
}

.mt-2 {
  margin-top: var(--space-sm);
}
</style>