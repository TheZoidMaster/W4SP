const owner = "JaegerwaldDev"; // Repository owner's username
const repo = "W4SP"; // Repository name
const filePath = "wiki/Main_Page.md"; // Path to the file
const branchName = "main"; // The branch name (e.g., "feature-branch")

const getCommitHistory = async () => {
    const url = `https://api.github.com/repos/${owner}/${repo}/commits?path=${filePath}&sha=${branchName}`;
    
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        const commits = await response.json();
        console.log(commits);
        return commits;
    } catch (error) {
        console.error("Failed to fetch commit history:", error);
    }
};

getCommitHistory();