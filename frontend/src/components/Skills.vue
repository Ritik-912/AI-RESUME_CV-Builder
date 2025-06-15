<template>
  <section class="section-form">
    <h2 class="section-title">Skills</h2>

    <div v-if="store.skills && store.skills.length">
      <div
        v-for="(group, groupIndex) in store.skills"
        :key="groupIndex"
        class="skill-group"
      >
        <h3>Skill Group {{ groupIndex + 1 }}</h3>
        <div class="form-group">
          <label :for="`group-name-${groupIndex}`">Group Name<span class="required-asterisk">*</span></label>
          <input
            :id="`group-name-${groupIndex}`"
            type="text"
            v-model.trim="group.group"
            class="form-control"
            placeholder="e.g. Programming Languages"
            required
          />
        </div>

        <div
          v-for="(skill, skillIndex) in group.members"
          :key="skillIndex"
          class="skill-entry"
        >
          <form @submit.prevent>
            <div class="form-group">
              <label :for="`skill-name-${groupIndex}-${skillIndex}`">Skill<span class="required-asterisk">*</span></label>
              <input
                :id="`skill-name-${groupIndex}-${skillIndex}`"
                type="text"
                v-model.trim="skill.name"
                class="form-control"
                placeholder="Enter skill name"
                required
              />
            </div>

            <div class="form-group">
              <label :for="`skill-level-${groupIndex}-${skillIndex}`">Proficiency Level<span class="required-asterisk">*</span></label>
              <select
                :id="`skill-level-${groupIndex}-${skillIndex}`"
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
              @click="removeSkill(groupIndex, skillIndex)"
            >
              Remove Skill
            </button>
          </form>
        </div>

        <button
          type="button"
          class="btn btn-secondary"
          @click="addSkill(groupIndex)"
        >
          Add Skill to {{ group.name || 'Group' }}
        </button>

        <button
          type="button"
          class="btn btn-danger mt-2"
          @click="removeGroup(groupIndex)"
        >
          Remove Group
        </button>

        <hr />
      </div>
    </div>
    <div v-else>
      <p>No skill groups added yet.</p>
    </div>

    <button
      type="button"
      @click="addGroup"
      class="btn btn-primary add-position-btn"
    >
      Add Skill Group
    </button>
  </section>
</template>

<script setup>
import { reactive } from 'vue'
import { useResume } from '../index.js'

const store = useResume()

function addGroup() {
  store.skills.push({
    group: '',
    members: [{ name: '', level: '' }]
  })
}

function removeGroup(groupIndex) {
  store.skills.splice(groupIndex, 1)
}

function addSkill(groupIndex) {
  store.skills[groupIndex].members.push({ name: '', level: '' })
}

function removeSkill(groupIndex, skillIndex) {
  store.skills[groupIndex].members.splice(skillIndex, 1)
}
</script>

<style scoped>
.skill-group {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 2px dashed var(--color-border, #d1d1d1);
  border-radius: 12px;
  background-color: #ffffff;
}

.skill-entry {
  margin: 1rem 0;
  padding: 1rem;
  border: 1px solid var(--color-border, #e0e0e0);
  border-radius: 8px;
  background-color: #f8f9fa;
}

.add-position-btn {
  width: 100%;
  margin-top: 1rem;
  font-size: 1.1rem;
}

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