assert result == "成功" and len(attempts) == 3, f"重试两次后成功：{result} {len(attempts)}"
