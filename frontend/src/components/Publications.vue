<template>
  <section class="section-form">
    <h2 class="section-title">Publications</h2>

    <div v-if="store.publications && store.publications.length">
      <div
        v-for="(publication, index) in store.publications"
        :key="index"
        class="publication-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`title-${index}`">Title</label>
            <input
              :id="`title-${index}`"
              type="text"
              class="form-control"
              v-model.trim="publication.title"
              placeholder="Enter publication title"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`publisher-${index}`">Publisher</label>
            <input
              :id="`publisher-${index}`"
              type="text"
              class="form-control"
              v-model.trim="publication.publisher"
              placeholder="Enter publisher name"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`publishedDate-${index}`">Published Date</label>
            <input
              :id="`publishedDate-${index}`"
              type="month"
              class="form-control"
              v-model="publication.publishedDate"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`link-${index}`">Link</label>
            <input
            :id="`link-${index}`"
            type="url"
            class="form-control"
            v-model="publication.link"
            />
          </div>

          <div class="form-group">
            <label :for="`abstract-${index}`">Abstract</label>
            <textarea
              :id="`abstract-${index}`"
              class="form-control"
              v-model="publication.abstract"
              rows="4"
              placeholder="Enter abstract or summary (optional)"
            ></textarea>
          </div>

          <div class="form-actions">
            <button
              type="button"
              class="btn btn-danger"
              v-if="store.publications.length > 1"
              @click="removePublication(index)"
            >
              Remove Publication
            </button>
          </div>
        </form>
      </div>
    </div>
    <div v-else>
      <p>No publications available.</p>
    </div>

    <button type="button" @click="addPublication" class="btn btn-primary add-position-btn">
      Add Publication
    </button>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'
import { useResume } from '../index.js'

const store = useResume()

function addPublication() {
  store.publications.push({
    title: '',
    publisher: '',
    publishedDate: '',
    link: null,
    abstract: ''
  })
}

function removePublication(index) {
  if (store.publications.length > 1) {
    store.publications.splice(index, 1)
  }
}

onMounted(() => {
  if (!store.publications || store.publications.length === 0) {
    store.publications = [
      {
        title: '',
        publisher: '',
        publishedDate: '',
        link: '',
        abstract: ''
      }
    ]
  }
});
</script>

<style scoped>
.publication-entry {
  margin-bottom: 2rem;
  padding: 1.5rem;
  border: 1px solid var(--color-border, #e0e0e0);
  border-radius: 8px;
  background-color: #f8f9fa;
  transition: all 0.3s ease;
}

.publication-entry:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.06);
  transform: translateY(-2px);
}

.add-position-btn {
  display: block;
  width: 100%;
  margin-top: 1rem;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .publication-entry {
    padding: 1rem;
  }

  .add-position-btn {
    font-size: 1rem;
  }
}
</style>