<template>
  <section class="section-form">
    <h2 class="section-title">Skills</h2>

    <div v-if="store.skills && store.skills.length">
      <div
        v-for="(skill, index) in store.skills"
        :key="index"
        class="skill-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`skill-name-${index}`">Skill<span class="required-asterisk">*</span></label>
            <input
              :id="`skill-name-${index}`"
              type="text"
              v-model.trim="skill.name"
              class="form-control"
              placeholder="Enter skill name"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`skill-level-${index}`">Proficiency Level<span class="required-asterisk">*</span></label>
            <select
              :id="`skill-level-${index}`"
              v-model="skill.level"
              class="form-control"
              required
            >
              <option disabled value="">Select proficiency</option>
              <option>Beginner</option>
              <option>Intermediate</option>
              <option>Advanced</option>
              <option>Expert</option>
            </select>
          </div>

          <button
            type="button"
            class="btn btn-danger"
            v-if="store.skills.length > 0"
            @click="removeSkill(index)"
          >
            Remove Skill
          </button>
        </form>
      </div>
    </div>
    <div v-else>
      <p>No skills added yet.</p>
    </div>

    <button
      type="button"
      @click="addSkill"
      class="btn btn-primary add-position-btn"
    >
      Add Skill
    </button>
  </section>
</template>

<script setup>
import { useResume } from '../index.js'
const store = useResume()

function addSkill() {
  store.skills.push({ name: '', level: '' })
}

function removeSkill(index) {
  if (store.skills.length > 0) {
    store.skills.splice(index, 1)
  }
}
</script>

<style scoped>
.skill-entry {
  margin-bottom: 2rem;
  padding: 1.5rem;
  border: 1px solid var(--color-border, #e0e0e0);
  border-radius: 8px;
  background-color: #f8f9fa;
  transition: all 0.3s ease;
}

.skill-entry:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.add-position-btn {
  width: 100%;
  margin-top: 1rem;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .skill-entry {
    padding: 1rem;
  }
}
</style>