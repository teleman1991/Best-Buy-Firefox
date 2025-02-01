                                self.logger.error("Failed to fill payment information.")
                        else:
                            self.logger.error("Checkout process failed.")
                    else:
                        self.logger.error("Failed to access cart.")
                else:
                    self.logger.error("Failed to add to cart.")
            else:
                self.logger.info("Item not in stock, checking again in 2 seconds...")
                time.sleep(2)

        self.logger.info("\nBot stopped - please complete your purchase!")
        input("Press Enter to exit...")

    def __del__(self):
        """Cleanup when object is destroyed"""
        try:
            if hasattr(self, 'driver'):
                self.driver.quit()
        except:
            pass