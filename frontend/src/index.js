import { defineStore } from "pinia";
export const useResume = defineStore("resume", {
  state: () => ({
    personalInfo: {
      name: '',
      email: '',
      phone: '',
      location: '',
      linkedin: '',
      github: '',
    },
    relevantCoursework: [],
    workExperiences: [],
    educations: [],
    certifications: [],
    awards: [],
    projects: [],
    volunteering: [],
    publications: [],
    languages: [],
    skills: [],
    jobDescription: '',
  }),
});