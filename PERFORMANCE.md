# Performance Tuning Guide

- Use async DB drivers and connection pooling.
- Enable Redis caching for repeated queries.
- Use pagination for large result sets.
- Monitor query execution time and flag slow queries.
- Scale backend and database containers horizontally.
- Use indexes on frequently queried columns.
- Tune DB configs (work_mem, innodb_buffer_pool, etc).
- Use CDN for frontend assets.
