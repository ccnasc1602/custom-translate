# -*- coding:utf-8 -*-
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create Handler
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)

# Create format
c_fomat = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s - %(message)s')
c_handler.setFormatter(c_fomat)

# Add handlers to the logger
logger.addHandler(c_handler)