<template>
  <section class="section-form">
    <h2 class="section-title">Work Experience</h2>

    <div v-if="store.workExperiences && store.workExperiences.length">
      <div
        v-for="(experience, index) in store.workExperiences"
        :key="index"
        class="experience-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`organization-${index}`">Organization</label>
            <input
              :id="`organization-${index}`"
              v-model.trim="experience.organization"
              type="text"
              class="form-control"
              placeholder="Enter organization name"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`position-${index}`">Position</label>
            <input
              :id="`position-${index}`"
              v-model.trim="experience.position"
              type="text"
              class="form-control"
              placeholder="Enter your role"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`startDate-${index}`">Start Date</label>
            <input
              :id="`startDate-${index}`"
              v-model="experience.startDate"
              type="month"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`endDate-${index}`">End Date</label>
            <input
              :id="`endDate-${index}`"
              v-model="experience.endDate"
              type="month"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`description-${index}`">Description</label>
            <textarea
              :id="`description-${index}`"
              v-model.trim="experience.description"
              class="form-control"
              placeholder="Summarize responsibilities or achievements"
              rows="4"
              required
            ></textarea>
          </div>

          <button
            type="button"
            class="btn btn-danger"
            @click="removeExperience(index)"
            v-if="store.workExperiences.length > 1"
          >
            Remove Experience
          </button>
        </form>
      </div>
    </div>
    <div v-else>
      <p>No work experiences available.</p>
    </div>

    <button type="button" class="btn btn-primary add-position-btn" @click="addExperience">
      Add New Experience
    </button>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'
import { useResume } from '../index.js'
const store = useResume()

const addExperience = () => {
  store.workExperiences.push({
    organization: '',
    position: '',
    startDate: '',
    endDate: '',
    description: ''
  })
}

const removeExperience = (index) => {
  if (store.workExperiences.length > 1) {
    store.workExperiences.splice(index, 1)
  }
}

onMounted(() => {
  if (!store.workExperiences || store.workExperiences.length === 0) {
    store.workExperiences = [
      {
        organization: '',
        position: '',
        startDate: '',
        endDate: '',
        description: ''
      }
    ]
  }
})
</script>

<style scoped>
.experience-entry {
  margin-bottom: 2rem;
  padding: 1.5rem;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background-color: #f8f9fa;
  transition: all 0.3s ease;
}

.experience-entry:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.add-position-btn {
  width: 100%;
  margin-top: 1rem;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .experience-entry {
    padding: 1rem;
  }
}
</style>