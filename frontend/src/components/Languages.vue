<template>
  <section class="section-form">
    <h2 class="section-title">Languages</h2>

    <div v-if="store.languages && store.languages.length">
      <div
        v-for="(language, index) in store.languages"
        :key="index"
        class="language-entry"
      >
        <div class="form-group">
          <label :for="'language-name-' + index">Language</label>
          <input
            :id="'language-name-' + index"
            type="text"
            v-model.trim="language.name"
            class="form-control"
            required
          />
        </div>

        <div class="form-group">
          <label :for="'language-level-' + index">Proficiency Level</label>
          <select
            :id="'language-level-' + index"
            v-model="language.level"
            class="form-control"
            required
          >
            <option disabled value="">Select proficiency</option>
            <option>Basic</option>
            <option>Conversational</option>
            <option>Fluent</option>
            <option>Native</option>
          </select>
        </div>

        <button
          v-if="store.languages.length > 1"
          @click="removeLanguage(index)"
          class="btn btn-danger"
        >
          Remove Language
        </button>
      </div>
    </div>
    <div v-else>
      <p>No languages added yet.</p>
    </div>

    <button @click="addLanguage" class="btn btn-primary w-full mt-4 text-lg">
      Add Language
    </button>
  </section>
</template>

<script setup>
import { onMounted } from 'vue';
import { useResume } from '../index.js';

const store = useResume();

function addLanguage() {
  store.languages.push({ name: '', level: '' });
}

function removeLanguage(index) {
  if (store.languages.length > 1) {
    store.languages.splice(index, 1);
  }
}

onMounted(() => {
  if (!store.languages || store.languages.length === 0) {
    store.languages = [{ name: '', level: '' }];
  }
});
</script>

<style scoped>
.languages-section {
  max-width: 700px;
  margin: 2rem auto;
  padding: 1rem;
}

.language-entry {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border-radius: 6px;
  background: #f9f9f9;
}

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
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  padding: 0.5rem 1rem;
  font-weight: 500;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 0.5rem;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-danger {
  background-color: #dc3545;
  color: #fff;
}

.btn-danger:hover {
  background-color: #c82333;
}
</style>