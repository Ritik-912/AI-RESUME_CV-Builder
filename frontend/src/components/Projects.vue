<template>
  <section class="section-form">
    <h2 class="section-title">Projects</h2>

    <div v-if="store.projects && store.projects.length">
      <div
        v-for="(project, index) in store.projects"
        :key="index"
        class="project-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`project-title-${index}`">Project Title<span class="required-asterisk">*</span></label>
            <input
              :id="`project-title-${index}`"
              type="text"
              v-model.trim="project.title"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`project-date-${index}`">Date<span class="required-asterisk">*</span></label>
            <input
              :id="`project-date-${index}`"
              type="month"
              v-model="project.date"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`project-tech-${index}`">Tech Stack</label>
            <input
              :id="`project-tech-${index}`"
              type="text"
              v-model="project.techStack"
              class="form-control"
            />
          </div>

          <div class="form-group">
            <label :for="`project-link-${index}`">Link</label>
            <input
              :id="`project-link-${index}`"
              type="url"
              v-model="project.link"
              class="form-control"
            />
          </div>

          <div class="form-group">
            <label :for="`project-desc-${index}`">Description</label>
            <textarea
              :id="`project-desc-${index}`"
              v-model="project.description"
              class="form-control"
              rows="3"
            ></textarea>
          </div>

          <button
            v-if="store.projects.length > 0"
            @click="removeProject(index)"
            type="button"
            class="btn btn-danger"
          >
            Remove Project
          </button>
        </form>
      </div>
    </div>
    <div v-else>
      <p>No projects available.</p>
    </div>

    <button @click="addProject" type="button" class="btn btn-primary w-full mt-4 text-lg">
      Add Project
    </button>
  </section>
</template>

<script setup>
import { useResume } from '../index.js'

const store = useResume()

function addProject() {
  store.projects.push({
    title: '',
    techStack: '',
    date: '',
    link: '',
    description: ''
  })
}

function removeProject(index) {
  if (store.projects.length > 0) {
    store.projects.splice(index, 1)
  }
}
</script>

<style scoped>

.project-entry {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1.5rem;
  background: #f9f9f9;
}
</style>
