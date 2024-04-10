// JavaScript for confirmation before deleting an animal
function confirmDelete(animalName, animalId) {
    if (confirm(`Are you sure you want to delete ${animalName}?`)) {
        window.location.href = `/delete-animal/${animalId}/`;
    }
}
