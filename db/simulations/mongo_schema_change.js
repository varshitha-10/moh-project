// Add new field to all user_profiles
const { MongoClient } = require('mongodb');
const uri = 'mongodb://user:password@mongo:27017';
const client = new MongoClient(uri);
async function run() {
  await client.connect();
  const db = client.db('testdb');
  // Add new field
  await db.collection('user_profiles').updateMany({}, { $set: { loyalty_status: 'bronze' } });
  // Add new collection
  await db.createCollection('user_feedback');
}
run().then(()=>client.close());
