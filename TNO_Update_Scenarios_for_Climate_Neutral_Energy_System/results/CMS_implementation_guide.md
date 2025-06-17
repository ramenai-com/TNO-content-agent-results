# CMS Implementation Guide - Climate Scenarios Content

## Overview
This guide provides clear instructions for implementing the improved climate scenarios content on the TNO website CMS.

## Content Files
- **English version**: `english_climate_scenarios_improved.md`
- **Dutch version**: `dutch_climate_scenarios_improved.md`

## Implementation Steps

### 1. Page Setup

#### For English Page:
- **URL**: `/en/sustainable/system-solutions-environment/transition-pathways/scenarios-climate-neutral-energy-system/`
- **Page Title**: "Scenarios for a Climate-Neutral Energy System"
- **Meta Description**: "Explore two pathways to climate neutrality by 2050. Choose between ADAPT's evolutionary approach or TRANSFORM's revolutionary transformation for your organization."

#### For Dutch Page:
- **URL**: `/nl/duurzaam/systeemoplossingen-omgeving-milieu/transitiepaden/scenario-klimaatneutraal-energiesysteem/`
- **Page Title**: "Scenario's voor een klimaatneutraal energiesysteem"
- **Meta Description**: "Ontdek twee routes naar klimaatneutraliteit in 2050. Kies tussen ADAPT's evolutionaire aanpak of TRANSFORM's revolutionaire transformatie voor uw organisatie."

### 2. Content Structure

#### Always Visible Content
The following sections should be visible when the page loads:
1. Main heading
2. Introduction paragraph ("Your Journey to Climate Neutrality...")
3. "Choose Your Path" section with brief overview

#### Accordion Sections
Create accordion blocks for each section marked with "🔽 ACCORDION":

1. **Understanding the Challenge / De uitdaging begrijpen**
   - Default state: Collapsed
   - Icon: Information or lightbulb icon

2. **Two Futures, Two Choices / Twee toekomsten, twee keuzes**
   - Default state: Collapsed
   - Icon: Fork/path icon
   - Consider making this expanded by default as it's core content

3. **Your Sector's Transformation Path / Het transformatiepad voor uw sector**
   - Default state: Collapsed
   - Icon: Industry/building icon
   - Sub-sections for each stakeholder type

4. **Critical Success Factors / Kritieke succesfactoren**
   - Default state: Collapsed
   - Icon: Star or checkmark icon

5. **Making It Real - Implementation Roadmap / Het werkelijkheid maken**
   - Default state: Collapsed
   - Icon: Calendar or roadmap icon

6. **Your Next Steps / Uw volgende stappen**
   - Default state: Collapsed
   - Icon: Arrow or steps icon

### 3. Styling Recommendations

#### Visual Design
- Use TNO brand colors for accordion headers
- Ensure sufficient contrast between expanded/collapsed states
- Add smooth transitions (0.3s) for accordion open/close
- Use consistent icons throughout

#### Typography
- Headers in accordions: One level below main page heading
- Use bold for scenario names (ADAPT/TRANSFORM)
- Bullet points for lists within accordions
- Clear visual hierarchy within each section

#### Interactive Elements
- Hover states for accordion headers
- Clear expand/collapse indicators (+/- or arrows)
- Keyboard accessible (Enter/Space to toggle)
- Mobile-friendly touch targets (min 44px height)

### 4. CMS Configuration

#### Accordion Block Settings
```
Block Type: Accordion
Title: [Section title without emoji]
Content: [Section content]
Default State: collapsed
Animation: slide
Duration: 300ms
Allow Multiple Open: yes
```

#### Content Formatting
- Remove the "🔽 ACCORDION:" prefix when entering in CMS
- Convert markdown formatting to CMS rich text
- Ensure proper heading hierarchy
- Maintain list formatting

### 5. Additional Features

#### Call-to-Action Buttons
Add CTA buttons for:
- Download full white paper
- Book consultation
- Access sector guides

#### Cross-linking
- Add language toggle between English/Dutch versions
- Link to related content and resources
- Ensure proper hreflang tags

#### Analytics Tracking
Track accordion interactions:
- Which sections are opened most
- Time spent in each section
- Conversion on CTAs

### 6. Mobile Optimization

Ensure accordions work well on mobile:
- Full-width accordion headers
- Larger touch targets
- Readable font sizes
- Proper spacing between sections

### 7. Testing Checklist

Before publishing:
- [ ] All accordions open/close properly
- [ ] Content is properly formatted in each section
- [ ] Links work correctly
- [ ] Mobile experience is smooth
- [ ] Page loads quickly
- [ ] Analytics tracking is active
- [ ] Both language versions are synchronized
- [ ] Cross-language links work

### 8. SEO Considerations

- Ensure all accordion content is crawlable
- Use semantic HTML (details/summary or proper ARIA)
- Include structured data for FAQ sections if applicable
- Maintain proper heading hierarchy even in accordions

## Final Notes

This improved structure transforms dense technical content into an engaging, interactive experience that guides different stakeholders through their climate transition journey. The accordion format allows users to explore relevant sections without being overwhelmed by the full content at once.