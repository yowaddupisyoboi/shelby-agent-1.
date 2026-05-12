class CryptoAnalyzer:

    def token_score(self, token_data):
        return {
            "token": token_data["token"],
            "score": (
                token_data["tx_volume_24h"] * 0.4 +
                token_data["active_wallets"] * 0.4 +
                token_data["liquidity_change"] * 1000
            )
        }

    def ecosystem_score(self, dev, social):
        return {
            "ecosystem": dev["ecosystem"],
            "score": dev["github_commits"] + dev["active_builders"] * 2 + social["trend_score"] * 1000
        }