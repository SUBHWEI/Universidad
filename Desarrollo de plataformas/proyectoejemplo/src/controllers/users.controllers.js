const userServices = require('../services/user.service');

exports.findAll = async (req, res) => {
    try {
        const users = await userServices.getAllUsers();
        res.status(200).json(users);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

exports.findById = async (req, res) => {
    try {
        const user = await userServices.getUserById(req.params.id);
        if (user) {
            res.status(200).json(user);
        } else {
            res.status(404).json({ message: 'User not found' });
        }
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};