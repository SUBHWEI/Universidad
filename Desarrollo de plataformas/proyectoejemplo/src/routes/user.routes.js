
const express = require('express');
const router = express.Router();
const userController = require('../controllers/users.controller');

router.get('/', userController.findAll);
router.get('/:id', userController.findById);
router.post('/', userController.createUser);
router.put('/:id', userController.update);
router.delete('/:id', userController.remove);

module.exports = router;