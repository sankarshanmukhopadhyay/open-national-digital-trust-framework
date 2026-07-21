---
layout: default
title: Documentation Conventions
parent: Documentation Architecture
nav_order: 4
---
# Documentation Conventions

## Reader-orientation metadata

Substantial pages should make the following clear in prose or a callout near the beginning:

- **Purpose:** why the page exists.
- **Before reading:** concepts or pages assumed.
- **After reading:** the logical next topic.
- **Reading time:** an approximate planning aid, not a performance target.

## Navigation contract

- Sidebar order groups reference material.
- Learning-path order communicates recommended study sequence.
- Breadcrumbs communicate structural ancestry.
- Previous and Next links communicate the active canonical sequence.
- Related reading communicates optional depth.

## Maintenance rule

A pull request that adds or substantially relocates documentation should update, where applicable:

1. the relevant parent index;
2. one or more learning paths;
3. `_data/learning_sequence.yml`;
4. the framework or concept dependency map;
5. local links and Jekyll navigation metadata.
