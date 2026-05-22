---
title: "Now open for building: Introducing Gemini CLI extensions"
source: "https://blog.google/technology/developers/gemini-cli-extensions/"
author:
  - "[[Taylor Mullen]]"
published: 2025-10-08
created: 2025-10-10
description: "Make Gemini CLI uniquely yours by connecting it to your everyday workflows and the tools you use most."
tags:
  - "clippings"
---
![Gemini CLI extensions hero image](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiCLI_Expand_Hero.width-800.format-webp.webp)

Gemini CLI extensions hero image

The best tools are the ones that adapt to you, not the other way around. For developers whose work is becoming more complex every day, the need for personalized, intelligent assistance has never been greater.

That’s why we’re announcing [Gemini CLI extensions](https://geminicli.com/extensions/), a new framework that allows you to customize Gemini CLI and connect it to the tools you use most, all from the command line. Instead of context-switching between your terminal and other tools, you can now bring those tools directly into your workflow.

In just three months since our [launch](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/), more than one million developers are building with Gemini CLI. And they can now access a new ecosystem of extensions from Google, plus industry leaders like Dynatrace, Elastic, Figma, Harness, Postman, Shopify, Snyk and Stripe, and the broader open-source community.

## Personalize your command line with Gemini CLI extensions

Gemini CLI is an open-source, AI-powered agent for your terminal, and extensions are its power-ups — pre-packaged, easily installable integrations that connect it to external tools including everything from databases and design platforms to payment services.

Each extension contains a built-in “playbook” that instantly teaches the AI how to use the new tools effectively. This means you get meaningful results from the very first command, no complex setup required, allowing you to tailor your experience with the tools most valuable to you.

It’s easy to install an extension — simply type: “gemini extensions install <add your GitHub URL or local path>” from your command line.

## Access an open, growing ecosystem of partners and builders

Extensions put Gemini CLI at the center of an open ecosystem in which anyone can build integrations. That’s why in addition to our own set of Google-created extensions, we’re launching with a strong group of partners and open-source contributors.

To make extensions easy to find and use, we’re also launching a new [Gemini CLI Extensions page](https://geminicli.com/extensions/). Here, you can discover a growing catalog of community, partner and Google-built extensions, ranked by popularity by GitHub stars.

You can get started with extensions from a wide range of launch partners and more coming soon. These include:

- [**Dynatrace**](https://github.com/dynatrace-oss/dynatrace-mcp): Get real-time insights into application performance, availability and root-cause analysis directly from your CLI to accelerate debugging.
- [**Elastic**](https://github.com/elastic/gemini-cli-elasticsearch): Search, retrieve and analyze Elasticsearch data in developer and agentic workflows. Connects directly to an Elastic MCP server hosted in Elastic Cloud Serverless.
- [**Figma**](https://github.com/figma/figma-gemini-cli-extension)**:** Generate code from frames, extract design context, retrieve resources and ensure design system consistency with your codebase.
- [**Harness**](https://github.com/harness/mcp-server): Bring AI-powered intelligence to CI/CD by analyzing pipeline execution data, surfacing cost insights, detecting failure patterns and automatically remediating issues to accelerate software delivery.
- [**Postman**](https://github.com/postmanlabs/postman-mcp-server/blob/main/gemini-extension.json)**:** Have AI agents access Postman workspaces, manage collections and environments, evaluate APIs and automate workflows through natural language interactions.
- [**Shopify**](https://github.com/Shopify/dev-mcp-gemini-cli)**:** Connect to Shopify's developer ecosystem with tools to search docs, explore API schemas, and build serverless Shopify functions.
- [**Snyk**](https://github.com/snyk/agentic-integration-wrappers): Seamlessly integrate Snyk's comprehensive security capabilities into your development process to ensure that code is secure at inception.
- [**Stripe**](https://github.com/stripe/agent-toolkit/blob/main/gemini-extension.json)**:** Define a set of tools that AI agents can use to interact with the Stripe API and search the knowledge base.

![Gemini CLI extension launch partners](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/extensions-partners-grid.width-1000.format-webp.webp)

Gemini CLI extension launch partners

## More than a connection: See how extensions add intelligence

Developers get more from Gemini CLI by integrating Model Context Protocol (MCP) tools, and extensions build on this by enabling even smarter interactions. While MCP provides the raw connection to a tool, a Gemini CLI extension takes the basic ability to use that tool and wraps it in a layer of intelligence and personalization. This makes the experience seamless for developers.

Gemini CLI extensions are easy to install and have a simple “playbook” — a set of tools it knows how to use, like a local script or a third-party API. When you run a command, Gemini CLI consults this playbook and uses the context from your environment (like your local files and git status) to execute the right tool for the job, exactly how you intended.

If you want to look under the hood, Gemini CLI extensions package instructions, MCP servers and custom commands into a familiar and user-friendly format. Extensions can bundle any combination of:

- **One or more MCP servers:** To connect with external tools and services.
- **Context files:** Like [GEMINI.md](https://github.com/google-gemini/gemini-cli/blob/93694c6a65dab0ac431b77bf6caadfea4c0e3c78/docs/cli/configuration.md#context-files-hierarchical-instructional-context) or bring your own context file type(s), to provide specific instructions and guidelines to the model.
- **Excluded tools:** Useful for disabling built-in tools or offering alternative implementations.
- **Custom commands:** To encapsulate complex prompts into simple slash commands.

## Discover Google-created extensions

Googlers have also been building a suite of extensions for Gemini CLI. Give them a try; they just might help you solve some common developer pain points, deepen integration with other Google offerings or just have fun:

For cloud-native deployments:

- Go from local code to a live public URL in a single step, with the [Cloud Run extension](https://github.com/GoogleCloudPlatform/cloud-run-mcp).
- Manage your Google Kubernetes Engine (GKE) clusters, from checking node health to deploying applications with our [GKE extension](https://github.com/GoogleCloudPlatform/gke-mcp).
- Give Gemini CLI the ability to easily interact with your Google Cloud environment by using the [gcloud extension](https://github.com/gemini-cli-extensions/gcloud).
- Understand, manage and troubleshoot your Google Cloud environment with the [Google Cloud Observability extension](https://github.com/gemini-cli-extensions/observability).

For app builders:

- Perform code reviews on your codebase with the [Code Review extension](https://github.com/gemini-cli-extensions/code-review).
- Perform AI-powered vulnerability detection on your code changes with the [Security extension](https://github.com/gemini-cli-extensions/security).
- Retrieve place info from Google and embed Google Maps imagery into applications with the [Google Maps Platform extension](https://github.com/googlemaps/platform-ai).
- Create, build, refactor, debug and maintain Flutter applications with the [Flutter extension](https://github.com/gemini-cli-extensions/flutter).
- Control and inspect a live Chrome browser for reliable automation, in-depth debugging and performance analysis with the [Chrome DevTools extension](https://github.com/ChromeDevTools/chrome-devtools-mcp).
- Set up and manage your Firebase backend with the [Firebase extension](https://github.com/gemini-cli-extensions/firebase).
- Enhance the user experience for building GenAI-powered apps with the [Genkit extension](https://github.com/gemini-cli-extensions/genkit).

For generative AI and data interaction:

- For a bit of fun, generate and edit images with the [Nano Banana extension](https://github.com/gemini-cli-extensions/nanobanana) 🍌.
- Explore and visualize your business data with the [Looker extension](https://github.com/gemini-cli-extensions/looker).
- Build applications and analyze trends with services like Cloud SQL, AlloyDB BigQuery and more with our [Data Cloud extensions](https://cloud.google.com/blog/products/databases/gemini-cli-extensions-for-google-data-cloud).
- Connect to enterprise data easily and securely using the [MCP Toolbox for Databases extension](https://github.com/gemini-cli-extensions/mcp-toolbox).

## Build the CLI of your dreams

Gemini CLI extensions put you in control. You can combine extensions, chain commands and build a personalized toolchain that perfectly fits the way you work.

Whether you want to streamline a personal workflow or integrate a company's internal tools, you now have the power to create the command-line experience you've always wanted.

Ready to get started? Visit the new [Gemini CLI Extensions page](https://geminicli.com/extensions/) to explore community tools, and check out our [templates](https://geminicli.com/docs/extensions/#extension-creation) and a [step-by-step guide](https://geminicli.com/docs/extensions/getting-started-extensions/) to help you build your first extension and share it with the community.