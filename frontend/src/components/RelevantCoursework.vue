<template>
  <section class="section-form">
    <h2 class="section-title">Relevant Coursework</h2>

    <div class="form-group">
      <label for="coursework-input">
        Relevant Coursework
      </label>
      <textarea
        id="coursework-input"
        v-model="courseworkInput"
        @input="updateCoursework"
        class="form-control"
        placeholder="Enter relevant coursework separated by commas (e.g., Data Structures, Algorithms, Database Systems, Web Development)"
        rows="4"
      ></textarea>
      <small class="help-text">Separate each course with a comma</small>
    </div>

    <div v-if="store.relevantCoursework && store.relevantCoursework.length" class="preview-section">
      <h3>Preview:</h3>
      <div class="coursework-tags">
        <span
          v-for="(course, index) in store.relevantCoursework"
          :key="index"
          class="coursework-tag"
        >
          {{ course }}
        </span>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useResume } from '../index.js';
import { ref } from 'vue';

const store = useResume();
const courseworkInput = ref('');

function updateCoursework() {
  if (courseworkInput.value.trim()) {
    // Split by comma, trim whitespace, and filter out empty strings
    store.relevantCoursework = courseworkInput.value
      .split(',')
      .map(course => course.trim())
      .filter(course => course.length > 0);
  } else {
    store.relevantCoursework = [];
  }
}
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-control {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  font-family: inherit;
}

.form-control:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}

.help-text {
  display: block;
  margin-top: 0.25rem;
  color: #6c757d;
  font-size: 0.875rem;
}

.preview-section {
  margin-top: 1.5rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 4px;
  border: 1px solid #e9ecef;
}

.preview-section h3 {
  margin: 0 0 1rem 0;
  font-size: 1.1rem;
  color: #495057;
}

.coursework-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.coursework-tag {
  background-color: #007bff;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 500;
}
</style>