# OAuth Debug Guide - Wardrobe Manager

## 🚨 Current Error
```
Unable to exchange external code
```

This error means:
- ✅ Google OAuth redirect is working
- ✅ User can select Google account
- ❌ Supabase cannot exchange the authorization code for a token
- ❌ This is a **Google Cloud Console configuration issue**

---

## 🔧 Fix: Google Cloud Console Configuration

### **Step 1: Access Google Cloud Console**
Go to: https://console.cloud.google.com/apis/credentials

### **Step 2: Find Your OAuth 2.0 Client**
- Look for: `<YOUR_CLIENT_ID>`
- Click the **edit icon** (pencil)

### **Step 3: Verify OAuth Consent Screen**
Go to: https://console.cloud.google.com/apis/credentials/consent

**Required Settings:**
- **User Type:** External (for testing)
- **App name:** a-wardrobe-manager (or whatever you named it)
- **Support email:** Your email
- **Authorized domains:** Leave blank for localhost testing
- **Scopes:** 
  - `userinfo.email`
  - `userinfo.profile`
  - `openid`

**Publishing Status:**
- Can be in "Testing" mode
- Add your email as a test user

### **Step 4: Fix Authorized Redirect URIs**
This is the **MOST CRITICAL** setting.

**In your OAuth 2.0 Client configuration:**

**Authorized redirect URIs (must be EXACTLY these):**
```
https://jtobhzxrcmmwrkffasrr.supabase.co/auth/v1/callback
```

**Authorized JavaScript origins:**
```
http://localhost:3000
http://localhost:3001
http://localhost:3002
```

⚠️ **IMPORTANT:**
- **NO trailing slashes** on redirect URI
- **HTTPS** for Supabase callback (not HTTP)
- **Exact match** - one character difference will fail

### **Step 5: Save and Wait**
- Click **SAVE**
- **Wait 5-10 minutes** for Google to propagate changes
- Sometimes takes up to 1 hour

---

## 🔍 Additional Checks

### **Check 1: Supabase Google OAuth Settings**
Go to: https://supabase.com/dashboard/project/jtobhzxrcmmwrkffasrr/auth/providers

Verify:
- ✅ Google provider is **ENABLED**
- ✅ Client ID: `<YOUR_CLIENT_ID>`
- ✅ Client Secret: `<YOUR_CLIENT_SECRET>`
- ✅ "Skip nonce check" is **OFF** (unchecked)

### **Check 2: Supabase Redirect URLs**
Go to: https://supabase.com/dashboard/project/jtobhzxrcmmwrkffasrr/auth/url-configuration

**Site URL:**
```
http://localhost:3000
```

**Redirect URLs:**
```
http://localhost:3000/auth/callback
http://localhost:3001/auth/callback
http://localhost:3002/auth/callback
```

Or use wildcard:
```
http://localhost:*/**
```

### **Check 3: Google Project Verification**
Go to: https://console.cloud.google.com/

Ensure:
- ✅ Project is the correct one
- ✅ OAuth consent screen is configured
- ✅ No quota limits exceeded
- ✅ Google+ API is enabled (legacy requirement)

---

## 🧪 Test After Configuration

### **1. Clear Everything**
```bash
# Browser
- Open DevTools (F12)
- Application → Storage → Clear site data
- Close browser completely
- Reopen browser

# Or use incognito mode
```

### **2. Check Browser Console**
When you try to sign in, check for:
```javascript
// In browser console (F12)
// Should show session after successful auth
localStorage.getItem('supabase.auth.token')
```

### **3. Test Sign-In Flow**
1. Go to http://localhost:3002
2. Click "Sign in with Google"
3. Select your Google account
4. Check URL after redirect:
   - ❌ If URL has `error=server_error` → Google config still wrong
   - ✅ If URL is `/dashboard` → Success!

---

## 🎯 Root Cause Analysis

The error `Unable to exchange external code` happens when:

1. **Wrong redirect URI** in Google Console
   - Most common cause
   - Must match EXACTLY what Supabase sends

2. **Client Secret mismatch**
   - Secret in Supabase doesn't match Google Console
   - Regenerate and update both sides

3. **OAuth Consent Screen issues**
   - App not published or in testing without test users
   - Missing required scopes

4. **Project/API issues**
   - Google+ API not enabled
   - Project quota exceeded

---

## 💡 Quick Fix Checklist

- [ ] Google OAuth Client ID exists and is correct
- [ ] Google OAuth Client Secret is correct (no extra spaces)
- [ ] Authorized redirect URI is **EXACTLY**: `https://jtobhzxrcmmwrkffasrr.supabase.co/auth/v1/callback`
- [ ] Authorized JavaScript origins include localhost ports
- [ ] OAuth consent screen is configured
- [ ] Your email is added as test user
- [ ] Changes saved and waited 5-10 minutes
- [ ] Browser cache cleared
- [ ] Tried in incognito mode

---

## 🔑 Double-Check These Values

**Google Client ID (from your creds):**
```
<YOUR_CLIENT_ID>
```

**Google Client Secret (from your creds):**
```
<YOUR_CLIENT_SECRET>
```

**Supabase Callback URL (MUST be in Google Console):**
```
https://jtobhzxrcmmwrkffasrr.supabase.co/auth/v1/callback
```

Make sure these match **EXACTLY** in both Google Console and Supabase.

---

## 🆘 If Still Not Working

### **Option 1: Regenerate OAuth Credentials**
1. Go to Google Cloud Console
2. Delete existing OAuth 2.0 Client
3. Create new OAuth 2.0 Client ID
4. Configure with correct redirect URIs
5. Update Supabase with new credentials

### **Option 2: Check Supabase Logs**
Go to: https://supabase.com/dashboard/project/jtobhzxrcmmwrkffasrr/logs/auth-logs

Look for specific error messages about why the exchange failed.

### **Option 3: Test with Different Google Account**
Sometimes specific accounts have issues. Try with another Gmail account.

---

## 📞 Need More Help?

If none of this works, provide:
1. Screenshot of Google OAuth Client configuration
2. Screenshot of Supabase Google Provider settings
3. Full error message from browser network tab
4. Auth logs from Supabase dashboard

