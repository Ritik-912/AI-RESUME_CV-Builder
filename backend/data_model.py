from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class LinkItem(BaseModel):
    text: str
    url: HttpUrl

class PersonalInfo(BaseModel):
    name: str
    email: EmailStr
    location: str
    links: Optional[List[LinkItem]] | None = None
    targetTitle: Optional[str] | None = None
    summary: Optional[str] | None = None

class WorkExperienceItem(BaseModel):
    organization: str
    position: str
    startDate: str
    endDate: Optional[str] | None = None
    description: Optional[str] | None = None

class EducationItem(BaseModel):
    instituteName: str
    courseName: str
    startDate: str
    endDate: Optional[str] | None = None
    grade: Optional[str] | None = None
    description: Optional[str] | None = None

class CertificationItem(BaseModel):
    title: str
    issuingAuthority: str
    issueDate: str

class AwardItem(BaseModel):
    title: str
    organization: str
    dateEarned: str

class ProjectItem(BaseModel):
    title: str
    organisation: Optional[str] | None = None
    startDate: str
    endDate: str
    link: Optional[HttpUrl] | None = None
    description: Optional[str] | None = None

class LanguageItem(BaseModel):
    name: str
    level: str

class VolunteeringItem(BaseModel):
    organization: str
    role: str
    startDate: str
    endDate: Optional[str] | None = None
    location: str
    description: Optional[str] | None = None

class PublicationItem(BaseModel):
    title: str
    publisher: str
    publishedDate: str
    abstract: Optional[str] | None = None
    link: Optional[HttpUrl] | None = None

class SkillItem(BaseModel):
    name: str
    level: str

class ResumeData(BaseModel):
    personalInfo: PersonalInfo
    workExperiences: Optional[List[WorkExperienceItem]] | None = None
    educations: Optional[List[EducationItem]] | None = None
    certifications: Optional[List[CertificationItem]] | None = None
    skills: Optional[List[SkillItem]] | None = None
    awards: Optional[List[AwardItem]] | None = None
    projects: Optional[List[ProjectItem]] | None = None
    languages: Optional[List[LanguageItem]] | None = None
    volunteering: Optional[List[VolunteeringItem]] | None = None
    publications: Optional[List[PublicationItem]] | None = None
    jobDescription: Optional[str] | None = None