# Auth testing (IRGS)
- Email/password: admin@irgs.app / chronicle123 (see /app/memory/test_credentials.md). POST /api/auth/login returns {user, token}; send Authorization: Bearer <token>.
- Google (Emergent-managed): create a test user + session in mongo (db from backend/.env DB_NAME):
  db.users.insertOne({user_id:'test-user-1', email:'test.user.1@example.com', name:'Test User', role:'player', auth:'google', created_at:new Date().toISOString()})
  db.user_sessions.insertOne({user_id:'test-user-1', session_token:'test_session_1', expires_at:new Date(Date.now()+7*864e5).toISOString(), created_at:new Date().toISOString()})
  Then use Authorization: Bearer test_session_1, or set cookie session_token (httpOnly, secure, sameSite None).
- Frontend stores token in localStorage key `irgs_token`.
