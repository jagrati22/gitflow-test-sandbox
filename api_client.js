// External API Fetcher Service

async function fetchUserProfile(userId) {
  // Bug: No response.ok check, no try-catch, prone to unhandled promise rejections
  const url = "https://api.example.com/users/" + userId;
  
  const response = await fetch(url);
  const data = await response.json();
  
  console.log("Fetched user data:", data);
  return data;
}

module.exports = { fetchUserProfile };
