import { create } from 'zustand';

export const browseState = create(() => ({}));

export function browseStateChange(val) {
	browseState.setState(val);
	console.log(browseState.getState(), 'browseState');
}
