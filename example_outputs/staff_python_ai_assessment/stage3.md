Stage 3 – System-design discussion

Example question:
“Architect a global, multi-tenant feature store service in Python that:
  - Ingests 100k events/sec from edge gateways across multiple regions.
  - Applies real-time transformations (e.g., joins with profile data in Redis).
  - Provides feature lookup APIs with low latency (<5ms) at scale.
  - Persists raw events to cold storage (e.g., S3) for replay.

Discuss:
  - Choice of frameworks (e.g., Faust, Kafka Streams, Pulsar) and data backends.
  - How to shard/partition tenants and handle hot keys.
  - Strong vs. eventual consistency trade-offs for feature reads.
  - Schema evolution strategy and backward compatibility.
  - Deployment across regions, disaster recovery, and failover.
  - Observability: metrics, tracing (e.g., OpenTelemetry), and alerting.
  - Fallback modes when downstream systems (Redis/S3) are unavailable.
”