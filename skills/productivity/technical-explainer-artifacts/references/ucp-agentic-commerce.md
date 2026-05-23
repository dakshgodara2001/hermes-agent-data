# Universal Commerce Protocol (UCP) explainer notes

Source session: user asked to read `https://ucp.dev/` and explain it simply with artifacts.

## Core summary

UCP = Universal Commerce Protocol. It is a common language/API standard for platforms, AI agents, businesses, and payment/credential providers to interoperate across commerce flows.

Plain-language one-liner:

> UCP lets an AI agent discover what a business supports, search/build a cart, checkout, pay securely, and manage orders using one shared protocol instead of a custom integration for every business.

## Why it exists

Agentic commerce requires AI agents and apps to transact across many merchants/services. Without a common protocol, every platform needs bespoke integrations with every merchant, checkout flow, payment system, order system, loyalty system, etc. UCP tries to standardize the interaction layer while keeping the business in control as merchant of record.

## Main actors

- **Platform**: consumes capabilities. Examples: AI shopping assistant, search engine, super app, procurement system, another business acting as buyer. It discovers and invokes business capabilities on behalf of a user/principal.
- **Business**: exposes capabilities. Examples: retailer, hotel, airline, restaurant, supplier. Usually remains merchant of record and retains transaction/customer control.
- **Credential Provider (CP)**: securely manages sensitive user data such as payment instruments, shipping address, identity credentials. Examples: digital wallets/identity providers.
- **Payment Service Provider (PSP)**: processes payments for the business. Examples: Stripe, Adyen, PayPal, Braintree.

## Key concepts

### Business profile

Businesses publish a machine-readable profile at:

```text
/.well-known/ucp
```

It declares services, capabilities, payment handlers, protocol versions, endpoints, schemas/spec URLs, and signing keys.

### Services

Broad vertical/API surfaces such as:

```text
dev.ucp.shopping
```

Future/roadmap verticals include food and lodging.

### Capabilities

Standalone features/verbs the business supports. Examples:

```text
dev.ucp.shopping.checkout
dev.ucp.shopping.cart
dev.ucp.shopping.catalog.search
dev.ucp.shopping.catalog.lookup
dev.ucp.shopping.order
dev.ucp.common.identity_linking
```

### Extensions

Optional add-ons that augment base capabilities. Examples:

- discount
- fulfillment/shipping
- buyer consent
- AP2 mandate
- loyalty/member benefits

Extensions declare parent capabilities and are pruned if their parent is not active.

### Capability negotiation

The business computes the active capability set by intersecting what the platform supports with what the business supports:

1. Match by capability name.
2. Select mutually supported version, usually latest compatible date.
3. Remove orphan extensions whose parent capability is not active.
4. Include active capabilities in responses.

Simple analogy: two parties choose the language both speak.

## Security and payment model

UCP uses standards like:

- OAuth 2.0 for identity/account linking.
- HTTP Message Signatures for permissionless request authentication.
- Public signing keys published in UCP profiles.
- PCI-DSS-compliant patterns for sensitive payment data handling.
- AP2 for cryptographic payment authorization in agent-led transactions.

Credentials should flow platform → business only; businesses must not echo credentials back in responses.

## UCP and AP2

AP2 = Agent Payments Protocol. UCP is compatible with AP2.

Useful distinction:

- **UCP**: commerce language — discovery, search, cart, checkout, orders, identity linking.
- **AP2**: trust/payment layer — signed intents, mandates, verifiable credentials, payment authorization bound to a specific checkout/cart state.

AP2 flow summary:

1. Business declares AP2 extension support.
2. Platform activates AP2 during checkout session.
3. Business signs checkout state.
4. User/platform generates mandates after consent.
5. Platform submits checkout/payment mandates to business.
6. Business and payment processor verify mandates.
7. Payment/order is confirmed.

Key benefit: payment authorization is mathematically tied to the exact cart/price/terms, reducing token replay and amount manipulation risk.

## Roadmap notes

UCP roadmap direction includes:

- Deeper consumer journey support: multi-item checkout, loyalty/member benefits, lifecycle management, cross-sell/upsell.
- Global markets: India, Indonesia, Latin America, localized payment interoperability.
- New industries: food and lodging.

Important caveat: roadmap is current direction, not a delivery commitment.

## Artifact examples that worked well

### Simple mental model

```text
Without UCP:
AI Agent → custom integration with every merchant/payment/order system

With UCP:
AI Agent → one common protocol → many businesses/payment providers
```

### Actor diagram

```text
User
  ↓
AI Agent / Platform
  ↓ UCP request
Business / Merchant
  ↓
Catalog / Checkout / Orders
  ↓
Payment + Credential layer
```

### Flow

```text
1. Discover business profile
2. Negotiate shared capabilities
3. Search/lookup products or services
4. Build cart/session
5. Checkout and confirm price/terms
6. Authorize payment, optionally via AP2
7. Complete order
8. Track/manage post-purchase
```

## Strategic framing

UCP is infrastructure for the agent era of commerce:

```text
Search era: user searches → website gets traffic
Marketplace era: user buys inside marketplace
Agent era: user gives intent → AI agent executes transaction
```

Strategic question: who owns the customer, checkout, authorization, and transaction data when agents become the interface? UCP’s framing keeps businesses central while making them machine-readable/actionable.
