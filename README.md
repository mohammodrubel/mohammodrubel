// app/dashboard/_dashboard_components/_GenarateResumeComponents/PdfTemplates.tsx
import React from 'react';
import {
  Document,
  Page,
  Text,
  View,
  StyleSheet,
  Font,
} from '@react-pdf/renderer';
import { Resume } from '@/lib/resume';

Font.register({
  family: 'Helvetica',
  fonts: [
    { src: 'https://fonts.gstatic.com/s/helveticaneue/v70/1Ptsg8zYS_SKggPNyCg4QIFqPfE.ttf', fontWeight: 400 },
    { src: 'https://fonts.gstatic.com/s/helveticaneue/v70/1Ptsg8zYS_SKggPNyCg4TYFqPfE.ttf', fontWeight: 700 },
  ],
});

Font.register({
  family: 'Courier',
  fonts: [
    { src: 'https://fonts.gstatic.com/s/courierprime/v9/u-450q2lgwslOqpF_6gQ8kELWwZjW-8.ttf', fontWeight: 400 },
  ],
});

// ─── TEMPLATE 1: EXECUTIVE ───────────────────────────────────────────────────
// A bold two-column executive layout with a deep navy sidebar and gold accents.
// Inspired by high-end print design — clean rule lines, strong type hierarchy.
export const ModernTemplate = ({ resume }: { resume: Resume }) => {
  const NAVY = '#0D1B2A';
  const GOLD = '#C9A84C';
  const GOLD_LIGHT = '#E8C97A';
  const SIDEBAR_TEXT = '#C8D6E5';
  const SIDEBAR_MUTED = '#6E8CAA';
  const BODY_DARK = '#1A2533';
  const BODY_MID = '#4A5568';
  const BODY_LIGHT = '#718096';
  const PAGE_BG = '#F7F6F2';

  const styles = StyleSheet.create({
    page: { flexDirection: 'row', backgroundColor: PAGE_BG, fontFamily: 'Helvetica' },
    sidebar: { width: '32%', backgroundColor: NAVY, paddingVertical: 44, paddingHorizontal: 28 },
    main: { width: '68%', paddingVertical: 44, paddingHorizontal: 36 },

    // Sidebar
    sName: { fontSize: 20, fontWeight: 'bold', color: '#FFFFFF', lineHeight: 1.2, marginBottom: 6 },
    sHeadline: { fontSize: 9, color: GOLD, letterSpacing: 2, textTransform: 'uppercase', marginBottom: 24 },
    sDivider: { height: 1, backgroundColor: GOLD, marginBottom: 20, opacity: 0.4 },
    sSectionLabel: { fontSize: 7, letterSpacing: 3, color: GOLD, textTransform: 'uppercase', marginBottom: 12, fontWeight: 'bold' },
    sContactRow: { flexDirection: 'row', marginBottom: 8, alignItems: 'flex-start' },
    sContactDot: { width: 4, height: 4, borderRadius: 2, backgroundColor: GOLD, marginTop: 4, marginRight: 8 },
    sContactText: { fontSize: 9, color: SIDEBAR_TEXT, flex: 1, lineHeight: 1.5 },
    sSkillRow: { flexDirection: 'row', alignItems: 'center', marginBottom: 7 },
    sSkillDot: { width: 3, height: 3, borderRadius: 2, backgroundColor: GOLD_LIGHT, marginRight: 8 },
    sSkillText: { fontSize: 10, color: SIDEBAR_TEXT },

    // Main
    mSectionLabel: {
      fontSize: 7, letterSpacing: 3, color: GOLD, textTransform: 'uppercase',
      fontWeight: 'bold', marginBottom: 14,
      borderBottomWidth: 1, borderBottomColor: GOLD, paddingBottom: 6,
    },
    mSummary: { fontSize: 11, color: BODY_MID, lineHeight: 1.8, marginBottom: 28 },
    expItem: { marginBottom: 20, paddingLeft: 14, borderLeftWidth: 2, borderLeftColor: '#D8D3C8' },
    expHeader: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 2 },
    expTitle: { fontSize: 13, fontWeight: 'bold', color: BODY_DARK },
    expDate: { fontSize: 8, color: GOLD, fontWeight: 'bold', letterSpacing: 1 },
    expCompany: { fontSize: 10, color: BODY_LIGHT, textTransform: 'uppercase', letterSpacing: 1.2, marginBottom: 6 },
    expDesc: { fontSize: 10, color: BODY_MID, lineHeight: 1.7 },
    eduItem: { marginBottom: 16 },
    eduHeader: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 2 },
    eduDegree: { fontSize: 12, fontWeight: 'bold', color: BODY_DARK },
    eduDate: { fontSize: 8, color: BODY_LIGHT, letterSpacing: 1 },
    eduSchool: { fontSize: 10, color: BODY_LIGHT, textTransform: 'uppercase', letterSpacing: 1 },
  });

  return (
    <Page size="LETTER" style={styles.page}>
      <View style={styles.sidebar}>
        <Text style={styles.sName}>{resume.personalInfo.fullName || 'Your Name'}</Text>
        {resume.professional.headline && (
          <Text style={styles.sHeadline}>{resume.professional.headline}</Text>
        )}
        <View style={styles.sDivider} />

        <Text style={styles.sSectionLabel}>Contact</Text>
        {resume.personalInfo.email && (
          <View style={styles.sContactRow}>
            <View style={styles.sContactDot} />
            <Text style={styles.sContactText}>{resume.personalInfo.email}</Text>
          </View>
        )}
        {resume.personalInfo.phone && (
          <View style={styles.sContactRow}>
            <View style={styles.sContactDot} />
            <Text style={styles.sContactText}>{resume.personalInfo.phone}</Text>
          </View>
        )}
        {resume.personalInfo.location && (
          <View style={styles.sContactRow}>
            <View style={styles.sContactDot} />
            <Text style={styles.sContactText}>{resume.personalInfo.location}</Text>
          </View>
        )}
        {resume.personalInfo.website && (
          <View style={styles.sContactRow}>
            <View style={styles.sContactDot} />
            <Text style={styles.sContactText}>{resume.personalInfo.website}</Text>
          </View>
        )}
        {resume.personalInfo.linkedin && (
          <View style={styles.sContactRow}>
            <View style={styles.sContactDot} />
            <Text style={styles.sContactText}>{resume.personalInfo.linkedin}</Text>
          </View>
        )}

        {resume.skills.length > 0 && (
          <View style={{ marginTop: 28 }}>
            <View style={styles.sDivider} />
            <Text style={styles.sSectionLabel}>Expertise</Text>
            {resume.skills.map((skill, i) => (
              <View key={i} style={styles.sSkillRow}>
                <View style={styles.sSkillDot} />
                <Text style={styles.sSkillText}>{skill}</Text>
              </View>
            ))}
          </View>
        )}
      </View>

      <View style={styles.main}>
        {resume.professional.summary && (
          <View style={{ marginBottom: 28 }}>
            <Text style={styles.mSectionLabel}>Profile</Text>
            <Text style={styles.mSummary}>{resume.professional.summary}</Text>
          </View>
        )}

        {resume.experience.length > 0 && (
          <View style={{ marginBottom: 28 }}>
            <Text style={styles.mSectionLabel}>Experience</Text>
            {resume.experience.map((job) => (
              <View key={job.id} style={styles.expItem}>
                <View style={styles.expHeader}>
                  <Text style={styles.expTitle}>{job.position}</Text>
                  <Text style={styles.expDate}>
                    {job.startDate} – {job.current ? 'Present' : job.endDate}
                  </Text>
                </View>
                <Text style={styles.expCompany}>{job.company}</Text>
                {job.description && <Text style={styles.expDesc}>{job.description}</Text>}
              </View>
            ))}
          </View>
        )}

        {resume.education.length > 0 && (
          <View>
            <Text style={styles.mSectionLabel}>Education</Text>
            {resume.education.map((edu) => (
              <View key={edu.id} style={styles.eduItem}>
                <View style={styles.eduHeader}>
                  <Text style={styles.eduDegree}>{edu.degree} in {edu.field}</Text>
                  <Text style={styles.eduDate}>{edu.graduationDate}</Text>
                </View>
                <Text style={styles.eduSchool}>{edu.school}</Text>
                {edu.description && <Text style={styles.expDesc}>{edu.description}</Text>}
              </View>
            ))}
          </View>
        )}
      </View>
    </Page>
  );
};

// ─── TEMPLATE 2: EDITORIAL ────────────────────────────────────────────────────
// A magazine-editorial style. Large oversized name, terracotta accents,
// clean serif-inspired hierarchy, and generous white space.
export const ClassicTemplate = ({ resume }: { resume: Resume }) => {
  const TERRA = '#B85C38';
  const TERRA_LIGHT = '#D4795A';
  const INK = '#1C1009';
  const INK_MID = '#4A3728';
  const INK_LIGHT = '#8C7B6E';
  const PAGE_BG = '#FDFAF5';
  const RULE = '#D9CFC4';

  const styles = StyleSheet.create({
    page: { backgroundColor: PAGE_BG, paddingHorizontal: 52, paddingVertical: 48, fontFamily: 'Helvetica' },

    // Header — full width, oversized name
    header: { marginBottom: 32 },
    topBar: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 12 },
    name: { fontSize: 42, fontWeight: 'bold', color: INK, letterSpacing: -1, lineHeight: 1 },
    headlineCol: { alignItems: 'flex-end' },
    headline: { fontSize: 10, color: TERRA, textTransform: 'uppercase', letterSpacing: 2 },
    headerRule: { height: 2, backgroundColor: INK, marginBottom: 10 },
    contactRow: { flexDirection: 'row', gap: 20, fontSize: 8.5, color: INK_LIGHT, letterSpacing: 0.5 },

    // Sections
    twoCol: { flexDirection: 'row', gap: 28 },
    mainCol: { flex: 2 },
    sideCol: { flex: 1 },

    sectionLabel: {
      fontSize: 7.5, letterSpacing: 3.5, textTransform: 'uppercase',
      color: TERRA, fontWeight: 'bold', marginBottom: 12,
    },
    thinRule: { height: 0.5, backgroundColor: RULE, marginBottom: 14 },

    summary: { fontSize: 11.5, color: INK_MID, lineHeight: 1.9, marginBottom: 28 },

    expItem: { marginBottom: 18 },
    expHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: 3 },
    expTitle: { fontSize: 13, fontWeight: 'bold', color: INK },
    expDate: { fontSize: 8, color: INK_LIGHT, letterSpacing: 0.8 },
    expCompany: { fontSize: 9.5, color: TERRA_LIGHT, fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 5 },
    expDesc: { fontSize: 10.5, color: INK_MID, lineHeight: 1.75 },

    skillPill: {
      fontSize: 9, color: TERRA, borderWidth: 0.5, borderColor: TERRA,
      paddingHorizontal: 10, paddingVertical: 4, marginBottom: 6, marginRight: 5,
    },
    skillsWrap: { flexDirection: 'row', flexWrap: 'wrap' },

    eduItem: { marginBottom: 14 },
    eduDegree: { fontSize: 11, fontWeight: 'bold', color: INK, marginBottom: 2 },
    eduMeta: { fontSize: 9, color: INK_LIGHT },
  });

  return (
    <Page size="LETTER" style={styles.page}>
      <View style={styles.header}>
        <View style={styles.topBar}>
          <Text style={styles.name}>{resume.personalInfo.fullName || 'Your Name'}</Text>
          {resume.professional.headline && (
            <View style={styles.headlineCol}>
              <Text style={styles.headline}>{resume.professional.headline}</Text>
            </View>
          )}
        </View>
        <View style={styles.headerRule} />
        <View style={styles.contactRow}>
          {resume.personalInfo.email && <Text>{resume.personalInfo.email}</Text>}
          {resume.personalInfo.phone && <Text>{resume.personalInfo.phone}</Text>}
          {resume.personalInfo.location && <Text>{resume.personalInfo.location}</Text>}
          {resume.personalInfo.website && <Text>{resume.personalInfo.website}</Text>}
          {resume.personalInfo.linkedin && <Text>{resume.personalInfo.linkedin}</Text>}
        </View>
      </View>

      {resume.professional.summary && (
        <View style={{ marginBottom: 28 }}>
          <Text style={styles.sectionLabel}>Profile</Text>
          <View style={styles.thinRule} />
          <Text style={styles.summary}>{resume.professional.summary}</Text>
        </View>
      )}

      <View style={styles.twoCol}>
        <View style={styles.mainCol}>
          {resume.experience.length > 0 && (
            <View style={{ marginBottom: 24 }}>
              <Text style={styles.sectionLabel}>Experience</Text>
              <View style={styles.thinRule} />
              {resume.experience.map((job) => (
                <View key={job.id} style={styles.expItem}>
                  <View style={styles.expHeader}>
                    <Text style={styles.expTitle}>{job.position}</Text>
                    <Text style={styles.expDate}>
                      {job.startDate} – {job.current ? 'Present' : job.endDate}
                    </Text>
                  </View>
                  <Text style={styles.expCompany}>{job.company}</Text>
                  {job.description && <Text style={styles.expDesc}>{job.description}</Text>}
                </View>
              ))}
            </View>
          )}
        </View>

        <View style={styles.sideCol}>
          {resume.skills.length > 0 && (
            <View style={{ marginBottom: 24 }}>
              <Text style={styles.sectionLabel}>Skills</Text>
              <View style={styles.thinRule} />
              <View style={styles.skillsWrap}>
                {resume.skills.map((skill, i) => (
                  <Text key={i} style={styles.skillPill}>{skill}</Text>
                ))}
              </View>
            </View>
          )}

          {resume.education.length > 0 && (
            <View>
              <Text style={styles.sectionLabel}>Education</Text>
              <View style={styles.thinRule} />
              {resume.education.map((edu) => (
                <View key={edu.id} style={styles.eduItem}>
                  <Text style={styles.eduDegree}>{edu.degree} in {edu.field}</Text>
                  <Text style={styles.eduMeta}>{edu.school}</Text>
                  <Text style={styles.eduMeta}>{edu.graduationDate}</Text>
                  {edu.description && <Text style={{ ...styles.expDesc, marginTop: 4 }}>{edu.description}</Text>}
                </View>
              ))}
            </View>
          )}
        </View>
      </View>
    </Page>
  );
};

// ─── TEMPLATE 3: MINIMALIST PRO ───────────────────────────────────────────────
// Ultra-clean Swiss/Bauhaus-inspired. Pure white, ink-black type, emerald green
// accents only for key labels. Every pixel intentional.
export const MinimalTemplate = ({ resume }: { resume: Resume }) => {
  const EMERALD = '#0D6E4F';
  const EMERALD_LIGHT = '#16A37A';
  const INK = '#0A0A0A';
  const MID = '#3D3D3D';
  const MUTED = '#888888';
  const RULE = '#E0E0E0';

  const styles = StyleSheet.create({
    page: { backgroundColor: '#FFFFFF', paddingHorizontal: 48, paddingVertical: 50, fontFamily: 'Helvetica' },

    // Header
    header: { marginBottom: 36 },
    name: { fontSize: 36, fontWeight: 'bold', color: INK, letterSpacing: -1.5, marginBottom: 6 },
    headlineRow: { flexDirection: 'row', alignItems: 'center', gap: 10, marginBottom: 18 },
    headlineBar: { width: 24, height: 2, backgroundColor: EMERALD },
    headlineText: { fontSize: 10, color: EMERALD, textTransform: 'uppercase', letterSpacing: 2 },
    contactRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 18 },
    contactItem: { fontSize: 9, color: MUTED, fontFamily: 'Courier' },

    rule: { height: 0.5, backgroundColor: RULE, marginBottom: 20, marginTop: 2 },

    // Sections
    section: { marginBottom: 26 },
    sLabel: {
      fontSize: 7, letterSpacing: 4, textTransform: 'uppercase',
      color: EMERALD, fontWeight: 'bold', marginBottom: 14,
    },

    summary: { fontSize: 11, color: MID, lineHeight: 1.85 },

    // Two-column layout
    twoCol: { flexDirection: 'row', gap: 36 },
    mainCol: { flex: 3 },
    sideCol: { flex: 1.5 },

    expItem: { marginBottom: 18, paddingBottom: 18, borderBottomWidth: 0.5, borderBottomColor: RULE },
    expHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: 2 },
    expTitle: { fontSize: 12.5, fontWeight: 'bold', color: INK },
    expDate: { fontSize: 8, color: MUTED, fontFamily: 'Courier' },
    expCompany: { fontSize: 9, color: EMERALD_LIGHT, fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 6 },
    expDesc: { fontSize: 10, color: MID, lineHeight: 1.7 },

    skillTag: {
      fontSize: 9, color: MID, borderWidth: 0.5, borderColor: RULE,
      paddingHorizontal: 8, paddingVertical: 3, marginBottom: 5, marginRight: 4,
      fontFamily: 'Courier',
    },
    skillsWrap: { flexDirection: 'row', flexWrap: 'wrap' },

    eduItem: { marginBottom: 14 },
    eduDegree: { fontSize: 11, fontWeight: 'bold', color: INK, marginBottom: 2 },
    eduSchool: { fontSize: 9, color: MUTED, marginBottom: 1 },
    eduDate: { fontSize: 8, color: MUTED, fontFamily: 'Courier' },
  });

  return (
    <Page size="LETTER" style={styles.page}>
      <View style={styles.header}>
        <Text style={styles.name}>{resume.personalInfo.fullName || 'Your Name'}</Text>
        {resume.professional.headline && (
          <View style={styles.headlineRow}>
            <View style={styles.headlineBar} />
            <Text style={styles.headlineText}>{resume.professional.headline}</Text>
          </View>
        )}
        <View style={styles.contactRow}>
          {resume.personalInfo.email && <Text style={styles.contactItem}>{resume.personalInfo.email}</Text>}
          {resume.personalInfo.phone && <Text style={styles.contactItem}>{resume.personalInfo.phone}</Text>}
          {resume.personalInfo.location && <Text style={styles.contactItem}>{resume.personalInfo.location}</Text>}
          {resume.personalInfo.website && <Text style={styles.contactItem}>{resume.personalInfo.website}</Text>}
          {resume.personalInfo.linkedin && <Text style={styles.contactItem}>{resume.personalInfo.linkedin}</Text>}
        </View>
      </View>

      <View style={styles.rule} />

      {resume.professional.summary && (
        <View style={styles.section}>
          <Text style={styles.sLabel}>Profile</Text>
          <Text style={styles.summary}>{resume.professional.summary}</Text>
        </View>
      )}

      <View style={styles.twoCol}>
        <View style={styles.mainCol}>
          {resume.experience.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sLabel}>Experience</Text>
              {resume.experience.map((job) => (
                <View key={job.id} style={styles.expItem}>
                  <View style={styles.expHeader}>
                    <Text style={styles.expTitle}>{job.position}</Text>
                    <Text style={styles.expDate}>
                      {job.startDate} – {job.current ? 'PRESENT' : job.endDate}
                    </Text>
                  </View>
                  <Text style={styles.expCompany}>{job.company}</Text>
                  {job.description && <Text style={styles.expDesc}>{job.description}</Text>}
                </View>
              ))}
            </View>
          )}
        </View>

        <View style={styles.sideCol}>
          {resume.skills.length > 0 && (
            <View style={{ ...styles.section, marginBottom: 20 }}>
              <Text style={styles.sLabel}>Skills</Text>
              <View style={styles.skillsWrap}>
                {resume.skills.map((skill, i) => (
                  <Text key={i} style={styles.skillTag}>{skill}</Text>
                ))}
              </View>
            </View>
          )}

          {resume.education.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sLabel}>Education</Text>
              {resume.education.map((edu) => (
                <View key={edu.id} style={styles.eduItem}>
                  <Text style={styles.eduDegree}>{edu.degree} in {edu.field}</Text>
                  <Text style={styles.eduSchool}>{edu.school}</Text>
                  <Text style={styles.eduDate}>{edu.graduationDate}</Text>
                  {edu.description && <Text style={{ ...styles.expDesc, marginTop: 4 }}>{edu.description}</Text>}
                </View>
              ))}
            </View>
          )}
        </View>
      </View>
    </Page>
  );
};
